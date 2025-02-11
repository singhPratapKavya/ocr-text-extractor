import base64
import json
import fitz  # PyMuPDF
import os
import time
from tkinter import Tk, filedialog
from .file_handler import create_output_folder
from .openai_handler import get_client

def select_files():
    """Prompts user to select multiple images or PDFs."""
    Tk().withdraw()  # Hide the root window
    file_paths = filedialog.askopenfilenames(filetypes=[("Images & PDFs", "*.jpg;*.jpeg;*.png;*.pdf")])

    if not file_paths:
        print("❌ No files selected. Please try again.")
        return None

    print(f"📂 Selected {len(file_paths)} files.")
    return file_paths

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

def run_ocr(file_paths):
    """Processes multiple documents and performs OCR on each."""
    if not file_paths:
        print("❌ No files provided. Exiting...")
        return

    print("🔄 Processing files...")
    time.sleep(1)

    # Create a main output directory for the batch run
    batch_output_dir = create_output_folder()
    
    for index, file_path in enumerate(file_paths, start=1):
        print(f"📄 Processing file {index}/{len(file_paths)}: {file_path}")

        file_extension = os.path.splitext(file_path)[1].lower()
        base64_image = None

        if file_extension in [".jpg", ".jpeg", ".png"]:
            base64_image = encode_image(file_path)
        elif file_extension == ".pdf":
            base64_image = extract_first_image_from_pdf(file_path)
            if not base64_image:
                print(f"❌ No images found in {file_path}. Skipping...")
                continue
        else:
            print(f"❌ Unsupported file format: {file_path}. Skipping...")
            continue

        print("✅ File encoded successfully! Preparing OCR request...")
        time.sleep(1)

        # Create an output directory for each file inside the batch folder
        file_output_dir = os.path.join(batch_output_dir, f"file_{index}")
        os.makedirs(file_output_dir, exist_ok=True)

        output_file = os.path.join(file_output_dir, "output.txt")
        full_response_file = os.path.join(file_output_dir, "full_response.json")

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
                        {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{base64_image}"}} if base64_image else None,
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

        print(f"🎉 OCR Complete for file {index}! Results saved to: {file_output_dir}")

    print(f"\n✅ All OCR processing completed! Results stored in: {batch_output_dir}")
