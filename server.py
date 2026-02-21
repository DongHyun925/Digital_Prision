import os
import traceback
from flask import Flask, request, jsonify, make_response
from flask_cors import CORS
from ai_engine import session_manager

app = Flask(__name__)

# --- Standard Flask-CORS Configuration ---
# This is the most robust way to handle CORS in Flask.
# It automatically handles OPTIONS requests and injects correct headers.
CORS(app, resources={r"/api/*": {"origins": "*"}}, supports_credentials=False)

@app.errorhandler(Exception)
def handle_exception(e):
    error_trace = traceback.format_exc()
    print(f"!!! SERVER ERROR !!!\n{error_trace}")
    return jsonify({
        "error": "Internal Server Error",
        "message": str(e),
        "traceback": error_trace
    }), 500

@app.route('/')
def health_check():
    return "🕸️ 404: THE DIGITAL PRISON - BACKEND SYSTEM ONLINE 🕸️"

@app.route('/api/ping', methods=['GET'])
def ping():
    return jsonify({"status": "pong", "message": "Connection stable"})

@app.route('/api/init', methods=['POST'])
def init_game():
    api_key = request.headers.get('X-Gemini-API-Key', '')
    session_manager.reset()
    session_manager.state['api_key'] = api_key
    return jsonify(session_manager.format_state_for_ui())

@app.route('/api/action', methods=['POST'])
def game_action():
    api_key = request.headers.get('X-Gemini-API-Key', '')
    data = request.get_json(silent=True) or {}
    user_input = data.get('command', '')
    
    print(f"ACTION REQUEST: {user_input}")
    session_manager.state['api_key'] = api_key
    ui_data = session_manager.process_action(user_input)
    return jsonify(ui_data)

@app.route('/api/hint', methods=['POST'])
def hint():
    api_key = request.headers.get('X-Gemini-API-Key', '')
    session_manager.state['api_key'] = api_key
    ui_data = session_manager.get_hint()
    return jsonify(ui_data)

@app.route('/api/load', methods=['POST'])
def load_game():
    api_key = request.headers.get('X-Gemini-API-Key', '')
    data = request.get_json(silent=True) or {}
    state_data = data.get('state')
    if not state_data:
        return jsonify({"error": "No save data"}), 400
    
    session_manager.state = state_data
    session_manager.state['api_key'] = api_key
    return jsonify(session_manager.format_state_for_ui())

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
