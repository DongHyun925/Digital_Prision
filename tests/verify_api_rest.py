import os
import requests
from dotenv import load_dotenv

# Load env
load_dotenv()
load_dotenv(os.path.join(os.path.dirname(__file__), "..", ".env"))

api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    print("Error: GOOGLE_API_KEY not found.")
else:
    print(f"Testing API Key via REST (starts with: {api_key[:5]}...)")
    
    # Try v1beta
    url = f"https://generativelanguage.googleapis.com/v1beta/models?key={api_key}"
    try:
        response = requests.get(url)
        print(f"\n[v1beta Response Code]: {response.status_code}")
        if response.status_code == 200:
            models = response.json().get('models', [])
            print(f"Available models (v1beta): {len(models)}")
            for m in models[:5]: # Show first 5
                print(f"- {m['name']}")
        else:
            print(f"Error: {response.text}")
    except Exception as e:
        print(f"Request failed: {str(e)}")

    # Try v1
    url_v1 = f"https://generativelanguage.googleapis.com/v1/models?key={api_key}"
    try:
        response_v1 = requests.get(url_v1)
        print(f"\n[v1 Response Code]: {response_v1.status_code}")
        if response_v1.status_code == 200:
            models_v1 = response_v1.json().get('models', [])
            print(f"Available models (v1): {len(models_v1)}")
            for m in models_v1[:5]:
                print(f"- {m['name']}")
        else:
            print(f"Error: {response_v1.text}")
    except Exception as e:
        print(f"Request failed: {str(e)}")
