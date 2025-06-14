import os
import shutil
from fastapi import UploadFile
import tempfile

UPLOAD_DIR = "./uploaded_pdfs"

def save_uploaded_files(files:list[UploadFile]) -> list[str]:
    """
    Save uploaded PDF files to a temporary directory and return their paths.
    
    Args:
        files (list[UploadFile]): List of uploaded files.
    
    Returns:
        list[str]: List of file paths where the PDFs are saved.
    """
    os.makedirs(UPLOAD_DIR, exist_ok=True)
    file_paths = []

    for file in files:
        temp_path = os.path.join(UPLOAD_DIR, file.filename)
        with open(temp_path, "wb") as f:
            shutil.copyfileobj(file.file, f)
        file_paths.append(temp_path)
    return file_paths
