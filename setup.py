from setuptools import setup, find_packages

setup(
    name="ocr_package",  # Name of the package
    version="0.1",  # Version number
    author="Kavya Pratap Singh",
    author_email="kavya.pratap.797@gmail.com",
    description="An OCR package for extracting text from images and PDFs",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    # url="https://github.com/yourusername/ocr_package",  # Replace with your GitHub repo
    packages=find_packages(),
    install_requires=[
        "openai>=1.0.0",
        "python-dotenv>=1.0.0",
        "PyMuPDF>=1.23.0",
        "pytest>=8.0.0",
        "tk",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
    python_requires=">=3.7",
)
