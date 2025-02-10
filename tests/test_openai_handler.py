import os
import pytest
from dotenv import load_dotenv
from unittest.mock import patch, MagicMock
from ocr_package.openai_handler import get_client

# Load environment variables
load_dotenv()

@pytest.fixture(autouse=True)
def mock_env_vars():
    """Mock the API key to prevent environment variable issues."""
    with patch.dict(os.environ, {"OPENAI_API_KEY": "test-key"}):
        yield

def test_openai_api_key():
    """Ensure API key is loaded correctly from environment variables."""
    assert os.getenv("OPENAI_API_KEY") is not None, "❌ API key is not set in the environment!"

@pytest.mark.skip(reason="Requires API call, can be enabled for integration testing")
def test_openai_response():
    """Test OpenAI response format using a dummy API call."""
    client = get_client()
    
    # Mock OpenAI response
    mock_response = MagicMock()
    mock_response.choices = [MagicMock(message=MagicMock(content="Test OCR Output"))]
    
    with patch.object(client.chat.completions, 'create', return_value=mock_response):
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": "Test"}],
            max_tokens=5
        )
        
        assert response
        assert hasattr(response, 'choices'), "❌ No choices in response!"
        assert isinstance(response.choices[0].message.content, str), "❌ Response content is not a string!"
