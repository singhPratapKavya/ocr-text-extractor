# OCR Package - Extract Text from Images & PDFs 

## 📌 Overview

This package allows users to perform OCR (Optical Character Recognition) and Handwriting Text Recognition (HTR) on images and PDFs.

- Automatically extracts text from uploaded documents.
- Supports image & PDF uploads.
- Applies spelling corrections for improved accuracy.
- Saves results in a structured output folder.
- User-friendly for Jupyter Notebook users with step-by-step execution.

## 📥 Installation

Before using the package, first clone the repository:

```bash
git clone https://github.com/your-username/ocr_package.git
cd ocr_package
```

Then install the package using: ```bash pip install .```


## 🛠️ Usage
Once installed, follow these steps:

#### Step 1: Set Up API Key (Only Needed Once)
```bash
import ocr_package
ocr_package.setup_api_key()
```
* This will prompt you to enter your OpenAI API key.
* The key is saved automatically for future use.

#### Step 2: Select a File
```bash
file_path = ocr_package.select_files()
```
* This will open a file dialog allowing you to select an image or PDF.
* The selected file's path will be stored in file_path.

#### Step 3: Run OCR
```bash
ocr_package.run_ocr(file_path)
```

This will:
* Process the selected document
* Display live progress updates (Loading..., Performing OCR..., etc.)
* Automatically save results inside a structured output folder.


## 📂 Output Files
After OCR processing, the results are saved in:
```bash
ocr_outputs/
│── run_YYYYMMDD_HHMMSS/
│   ├── output.txt          # Extracted and refined text
│   ├── full_response.json  # Raw response from OpenAI
```

## 🧪 Running Tests (tests/ Folder)

This package includes unit tests to ensure functionality.

Run all tests:
```bash
python -m pytest tests/
```
### ✔ Test Coverage

| Test File               | Purpose                                      |
|-------------------------|----------------------------------------------|
| `test_file_handler.py`  | Ensures output folders are created correctly. |
| `test_ocr_processing.py` | Tests file selection & image encoding.       |
| `test_openai_handler.py` | Ensures API key handling & OpenAI calls work correctly. |


## 🔧 Troubleshooting

1️⃣ OpenAI API Key Not Found

```bash
ValueError: API key is missing. Please run `setup_api_key()`.
```
Solution:
Run ```bash import ocr_package```
```bash ocr_package.setup_api_key()``` again. 

✅ This will prompt you to enter your API key. Once saved, you won’t need to enter it again.


2️⃣ OpenAI API Key Keeps Asking Again
Issue:
If the API key keeps asking for input, it may be due to a corrupted or missing .env file.
Solution: Reset your API key by running:

```bash
import os
import shutil

# Delete the stored API key
shutil.rmtree(os.path.expanduser("~/.ocr_package"), ignore_errors=True)

# Run setup again
import ocr_package
ocr_package.setup_api_key()
```

✅ This will delete any previous key and allow you to enter it again securely.

3️⃣ File Selection Not Working
If no file selection dialog appears, ensure:

* Your Python environment supports Tkinter (tk).
* You're running the code in a GUI-supported environment (not a headless server).

## 📌 Contributing
Want to improve this package?
Feel free to fork the repo, create a new branch, and submit a pull request!

1️⃣ Fork the repository
2️⃣ Clone your fork
```bash
git clone https://github.com/your-username/ocr_package.git
cd ocr_package
```
3️⃣ Create a new branch
```bash
git checkout -b feature-new-update
```
4️⃣ Make changes & commit
```bash
git add .
git commit -m "Added new feature"
```
5️⃣ Push changes & create a pull request
```bash
git push origin feature-new-update
```







