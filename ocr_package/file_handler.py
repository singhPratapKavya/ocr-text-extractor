import os
from datetime import datetime

def create_output_folder():
    """Creates a new folder with a timestamp for each run."""
    base_dir = os.path.join(os.getcwd(), "ocr_outputs")
    os.makedirs(base_dir, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_dir = os.path.join(base_dir, f"run_{timestamp}")
    os.makedirs(output_dir)

    return output_dir
