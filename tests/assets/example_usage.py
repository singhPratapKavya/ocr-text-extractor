from ocr_app.main import select_file, encode_image, extract_first_image_from_pdf

# Example usage of the package
file_path = select_file()
print(f"Selected file: {file_path}")

if file_path.endswith((".jpg", ".jpeg", ".png")):
    encoded_image = encode_image(file_path)
    print(f"Encoded image: {encoded_image[:50]}...")  # Print partial output for readability

elif file_path.endswith(".pdf"):
    encoded_image = extract_first_image_from_pdf(file_path)
    if encoded_image:
        print("Extracted image from PDF and encoded successfully.")
    else:
        print("No image found in the provided PDF.")