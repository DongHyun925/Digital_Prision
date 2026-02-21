from flask import Flask, request, jsonify, make_response
from flask_cors import CORS
import traceback
import sys
from ai_engine import session_manager

app = Flask(__name__)
# CORS 설정을 최대한 허용
CORS(app)

@app.before_request
def handle_options():
    # OPTIONS 요청(Preflight)에 대해 즉시 200 응답과 헤더를 반환하여 브라우저 차단 방지
    if request.method == 'OPTIONS':
        response = make_response()
        response.headers.add('Access-Control-Allow-Origin', '*')
        response.headers.add('Access-Control-Allow-Headers', '*')
        response.headers.add('Access-Control-Allow-Methods', '*')
        return response

@app.after_request
def add_cors_headers(response):
    # 모든 응답에 CORS 헤더 강제 주입
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,X-Gemini-API-Key,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
    return response

@app.errorhandler(Exception)
def handle_any_error(e):
    # 어떤 에러가 나도 CORS 헤더와 함께 상세 원인을 JSON으로 반환
    error_msg = str(e)
    error_type = type(e).__name__
    error_trace = traceback.format_exc()
    print(f"!!! GLOBAL ERROR !!!\n{error_trace}")
    
    response = jsonify({
        "error": "Backend Error",
        "message": error_msg,
        "type": error_type,
        "traceback": error_trace
    })
    response.status_code = 500
    # 에러 응답에도 강제로 헤더 추가 (after_request가 안 불릴 경우 대비)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/')
def health_check():
    return "🕸️ 404: THE DIGITAL PRISON - BACKEND SYSTEM ONLINE 🕸️"

@app.route('/api/ping')
def ping():
    return jsonify({"status": "pong", "message": "Connection stable"})

@app.route('/api/init', methods=['POST'])
def init_game():
    api_key = request.headers.get('X-Gemini-API-Key', '')
    state = session_manager.reset()
    session_manager.state['api_key'] = api_key
    return jsonify(session_manager.format_state_for_ui())

@app.route('/api/action', methods=['POST'])
def game_action():
    api_key = request.headers.get('X-Gemini-API-Key', '')
    # JSON 파싱 오류 방지를 위해 silent=True 사용
    data = request.get_json(silent=True) or {}
    user_input = data.get('command', '')
    
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
        response = jsonify({"error": "No save data"})
        response.status_code = 400
        return response
    
    session_manager.state = state_data
    session_manager.state['api_key'] = api_key
    return jsonify(session_manager.format_state_for_ui())

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
