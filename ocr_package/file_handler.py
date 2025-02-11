import os
from datetime import datetime

def create_output_folder():
    """Creates a new main folder for a batch run with a timestamp."""
    base_dir = os.path.join(os.getcwd(), "ocr_outputs")
    os.makedirs(base_dir, exist_ok=True)

    # Create a main batch folder with timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    batch_output_dir = os.path.join(base_dir, f"run_{timestamp}")
    os.makedirs(batch_output_dir)

    return batch_output_dir  # Return the main batch folder path
