import os
import pytest
import base64
from unittest.mock import patch
from ocr_package.ocr_processing import encode_image, extract_first_image_from_pdf, select_file

# Sample test files (moved from `examples/` to `tests/assets/`)
TEST_IMAGE_PATH = "tests/assets/sample_image.png"
TEST_PDF_PATH = "tests/assets/sample_document.pdf"

def test_encode_image():
    """Test if an image file is correctly encoded to Base64."""
    assert os.path.exists(TEST_IMAGE_PATH), "❌ Test image not found!"
    
    encoded_image = encode_image(TEST_IMAGE_PATH)
    assert isinstance(encoded_image, str)
    assert len(encoded_image) > 0
    assert base64.b64decode(encoded_image)  # Ensure valid Base64 encoding

def test_extract_first_image_from_pdf():
    """Test extracting an image from a PDF file."""
    assert os.path.exists(TEST_PDF_PATH), "❌ Test PDF not found!"
    
    encoded_image = extract_first_image_from_pdf(TEST_PDF_PATH)
    assert isinstance(encoded_image, str)
    assert len(encoded_image) > 0

@pytest.mark.skip(reason="Manual user interaction required")
def test_select_file(monkeypatch):
    """Mock user input for file selection."""
    monkeypatch.setattr('tkinter.filedialog.askopenfilename', lambda: TEST_IMAGE_PATH)
    file_path = select_file()
    assert file_path == TEST_IMAGE_PATH
