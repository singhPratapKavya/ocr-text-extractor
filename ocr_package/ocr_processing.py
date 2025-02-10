import base64
import json
import fitz  # PyMuPDF
import os
import time
from tkinter import Tk, filedialog
from .file_handler import create_output_folder
from .openai_handler import get_client

def select_file():
    """Prompts user to select an image or PDF file."""
    Tk().withdraw()  # Hide the root window
    file_path = filedialog.askopenfilename(filetypes=[("Images & PDFs", "*.jpg;*.jpeg;*.png;*.pdf")])

    if not file_path:
        print("❌ No file selected. Please try again.")
        return None

    print(f"📂 Selected file: {file_path}")
    return file_path

def encode_image(image_path):
    """Encodes an image as a Base64 string."""
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")

def extract_first_image_from_pdf(pdf_path):
    """Extracts the first image from a PDF file and returns its Base64 encoding."""
    doc = fitz.open(pdf_path)
    for page in doc:
        images = page.get_images(full=True)
        if images:
            xref = images[0][0]  # Get first image
            base_image = doc.extract_image(xref)
            image_bytes = base_image["image"]
            return base64.b64encode(image_bytes).decode("utf-8")
    return None  # No image found in PDF

def run_ocr(file_path):
    """Processes the selected document and performs OCR with live updates."""
    if not file_path:
        print("❌ No file provided. Exiting...")
        return

    print("🔄 Processing file...")
    time.sleep(1)

    file_extension = os.path.splitext(file_path)[1].lower()

    if file_extension in [".jpg", ".jpeg", ".png"]:
        base64_image = encode_image(file_path)
    elif file_extension == ".pdf":
        base64_image = extract_first_image_from_pdf(file_path)
        if not base64_image:
            print("❌ No images found in the PDF. Exiting...")
            return
    else:
        print("❌ Unsupported file format. Please upload a JPG, PNG, or PDF.")
        return

    print("✅ File encoded successfully! Preparing OCR request...")
    time.sleep(1)

    # Create structured output directory
    output_dir = create_output_folder()
    output_file = os.path.join(output_dir, "output.txt")
    full_response_file = os.path.join(output_dir, "full_response.json")

    print("🚀 Sending request to OpenAI...")
    time.sleep(1)

    # Get OpenAI client
    client = get_client()

    # Send to OpenAI
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": "Perform OCR and handwriting text recognition (HTR) on the provided document. Extract all text accurately, correct spelling mistakes, and structure the output in a clear, readable format."},
                    {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{base64_image}"}},
                ],
            }
        ],
        max_tokens=500,
    )

    # Process the extracted text
    extracted_text = response.choices[0].message.content.strip().replace("\n\n", "\n").replace("\n---\n", "")

    # Save output files
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(extracted_text)

    with open(full_response_file, "w", encoding="utf-8") as f:
        json.dump(response.model_dump(), f, indent=4)

    print(f"🎉 OCR Complete! Results saved to: {output_dir}")
