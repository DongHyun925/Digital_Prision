import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load env
load_dotenv()
load_dotenv(os.path.join(os.path.dirname(__file__), "..", ".env"))

api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    print("Error: GOOGLE_API_KEY not found in environment.")
else:
    print(f"API Key found (starts with: {api_key[:5]}...)")
    genai.configure(api_key=api_key)
    
    try:
        print("Listing available models...")
        for m in genai.list_models():
            if 'generateContent' in m.supported_generation_methods:
                print(f"- {m.name} (Display: {m.display_name})")
    except Exception as e:
        print(f"Error listing models: {str(e)}")
