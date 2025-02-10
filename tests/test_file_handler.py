import os
import pytest
from ocr_package.file_handler import create_output_folder

def test_create_output_folder():
    """Test if output folder is created successfully and follows naming convention."""
    output_dir = create_output_folder()
    
    assert os.path.exists(output_dir), "❌ Output directory was not created!"
    assert os.path.isdir(output_dir), "❌ Output path is not a directory!"
    
    # Check that folder name starts with "run_" and contains a timestamp
    assert os.path.basename(output_dir).startswith("run_"), "❌ Folder name format is incorrect!"
