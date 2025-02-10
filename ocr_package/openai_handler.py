import os
from dotenv import load_dotenv, set_key
from openai import OpenAI

# Define `.env` path
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
ENV_PATH = os.path.join(BASE_DIR, ".env")

# Load environment variables
load_dotenv(dotenv_path=ENV_PATH, override=True)

def setup_api_key():
    """Prompt user for API key and save it securely."""
    api_key = os.getenv("OPENAI_API_KEY")

    if not api_key:
        api_key = input("🔑 Enter your OpenAI API key: ").strip()
        set_key(ENV_PATH, "OPENAI_API_KEY", api_key)
        print("✅ API key saved successfully!")

    return api_key

def get_client():
    """Return OpenAI client with a valid API key."""
    api_key = os.getenv("OPENAI_API_KEY") or setup_api_key()

    if not api_key:
        raise ValueError("❌ API key is missing. Please run `setup_api_key()`.")

    return OpenAI(api_key=api_key)
