import os
import getpass  # Secure input without displaying characters
from dotenv import load_dotenv, set_key
from openai import OpenAI

# Define a persistent global `.env` path (HOME directory)
HOME_ENV_DIR = os.path.join(os.path.expanduser("~"), ".ocr_package")
ENV_PATH = os.path.join(HOME_ENV_DIR, ".env")

# Ensure `.env` directory exists
os.makedirs(HOME_ENV_DIR, exist_ok=True)

def setup_api_key():
    """Prompt user for API key once and save it persistently."""
    load_dotenv(dotenv_path=ENV_PATH, override=True)  # Ensure the .env file is loaded
    api_key = os.getenv("OPENAI_API_KEY")

    if api_key:
        print("✅ OpenAI API Key Authenticated")  # 🔹 Instead of printing the key
    else:
        print("🔑 OpenAI API Key is required to use this package.")
        api_key = getpass.getpass("🔒 Enter your OpenAI API key: ").strip()  # Hides input
        set_key(ENV_PATH, "OPENAI_API_KEY", api_key)
        print("✅ API key saved successfully!")

    return api_key

def get_client():
    """Return OpenAI client with a valid API key, ensuring it is only set once."""
    load_dotenv(dotenv_path=ENV_PATH, override=True)  # Load .env file before retrieving API key
    api_key = os.getenv("OPENAI_API_KEY")

    if not api_key:
        api_key = setup_api_key()  # If not set, ask user to enter API key once

    return OpenAI(api_key=api_key)
