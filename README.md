OCR Package - Extract Text from Images & PDFs Using OpenAI 🚀
📌 Overview
This package allows users to perform OCR (Optical Character Recognition) and Handwriting Text Recognition (HTR) on images and PDFs using OpenAI’s GPT models.

🔹 Automatically extracts text from uploaded documents.
🔹 Supports image & PDF uploads.
🔹 Applies spelling corrections for improved accuracy.
🔹 Saves results in a structured output folder.
🔹 User-friendly for Jupyter Notebook users with step-by-step execution.

📥 Installation
Before using the package, install it using:

bash
Copy
Edit
pip install ocr_package
✅ This will install all required dependencies.

⚙️ Dependencies (requirements.txt)
This package requires the following dependencies:

txt
Copy
Edit
openai>=1.0.0
python-dotenv>=1.0.0
PyMuPDF>=1.23.0
pytest>=8.0.0
tk
Install them manually if needed:

bash
Copy
Edit
pip install -r requirements.txt
🛠️ Usage in Jupyter Notebook
Once installed, follow these steps:

Step 1: Set Up API Key (Only Needed Once)
python
Copy
Edit
import ocr_package
ocr_package.setup_api_key()
🔹 This will prompt you to enter your OpenAI API key.
🔹 The key is saved automatically for future use.

Step 2: Select a File
python
Copy
Edit
file_path = ocr_package.select_file()
📂 This will open a file dialog allowing you to select an image or PDF.
📂 The selected file's path will be stored in file_path.

Step 3: Run OCR
python
Copy
Edit
ocr_package.run_ocr(file_path)
🚀 This will:
✅ Process the selected document
✅ Display live progress updates (Loading..., Performing OCR..., etc.)
✅ Automatically save results inside a structured output folder.

📂 Output Files
After OCR processing, the results are saved in:

bash
Copy
Edit
ocr_outputs/
│── run_YYYYMMDD_HHMMSS/
│   ├── output.txt          # Extracted and refined text
│   ├── full_response.json  # Raw response from OpenAI
📌 The folder is automatically created with a timestamp for every run.

🧪 Running Tests (tests/ Folder)
This package includes unit tests to ensure functionality.

Run all tests:

bash
Copy
Edit
python -m pytest tests/
✔ Test Coverage
Test File	Purpose
test_file_handler.py	Ensures output folders are created correctly.
test_ocr_processing.py	Tests file selection & image encoding.
test_openai_handler.py	Ensures API key handling & OpenAI calls work correctly.
Skipping Tests (Optional)
Some tests require manual input (file selection) or real OpenAI API calls.
To skip them, run:

bash
Copy
Edit
python -m pytest tests/ --disable-warnings
🔧 Troubleshooting
1️⃣ OpenAI API Key Not Found
Error:

vbnet
Copy
Edit
ValueError: API key is missing. Set OPENAI_API_KEY in your environment.
Solution:

Run ocr_package.setup_api_key() again.
2️⃣ pytest Command Not Found
If pytest isn't recognized, try:

bash
Copy
Edit
python -m pytest tests/
or manually install pytest:

bash
Copy
Edit
pip install pytest
3️⃣ File Selection Not Working
If no file selection dialog appears, ensure:

Your Python environment supports Tkinter (tk).
You're running the code in a GUI-supported environment (not a headless server).
📌 Contributing
Want to improve this package?
Feel free to fork the repo, create a new branch, and submit a pull request!

1️⃣ Fork the repository
2️⃣ Clone your fork

bash
Copy
Edit
git clone https://github.com/your-username/ocr_package.git
cd ocr_package
3️⃣ Create a new branch

bash
Copy
Edit
git checkout -b feature-new-update
4️⃣ Make changes & commit

bash
Copy
Edit
git add .
git commit -m "Added new feature"
5️⃣ Push changes & create a pull request

bash
Copy
Edit
git push origin feature-new-update
