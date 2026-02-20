import os
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

# Load env
load_dotenv()
load_dotenv(os.path.join(os.path.dirname(__file__), "..", ".env"))

api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    print("Error: GOOGLE_API_KEY not found.")
else:
    print(f"API Key exists. Testing models...")
    models = ["gemini-2.0-flash", "gemini-1.5-flash", "gemini-1.5-pro"]
    
    for model_name in models:
        try:
            llm = ChatGoogleGenerativeAI(model=model_name, google_api_key=api_key)
            res = llm.invoke("Hi")
            print(f"✅ {model_name}: Success")
        except Exception as e:
            print(f"❌ {model_name}: Failed - {str(e)}")
