import os
import getpass  # Secure input without displaying characters
from dotenv import load_dotenv, set_key
from openai import OpenAI

# Define a persistent global `.env` path (HOME directory)
HOME_ENV_DIR = os.path.join(os.path.expanduser("~"), ".ocr_package")
ENV_PATH = os.path.join(HOME_ENV_DIR, ".env")

# Ensure `.env` directory exists
os.makedirs(HOME_ENV_DIR, exist_ok=True)

# Load environment variables
load_dotenv(dotenv_path=ENV_PATH, override=True)

def setup_api_key():
    """Prompt user for API key once and save it persistently."""
    api_key = os.getenv("OPENAI_API_KEY")

    if not api_key:
        print("🔑 OpenAI API Key is required to use this package.")
        api_key = getpass.getpass("🔒 Enter your OpenAI API key: ").strip()  # Hides input
        set_key(ENV_PATH, "OPENAI_API_KEY", api_key)
        print("✅ API key saved successfully!")

    return api_key

def get_client():
    """Return OpenAI client with a valid API key without prompting again."""
    api_key = os.getenv("OPENAI_API_KEY") or setup_api_key()

    if not api_key:
        raise ValueError("❌ API key is missing. Please run `setup_api_key()`.")

    return OpenAI(api_key=api_key)
