import requests
from client.config import API_URL

def upload_pdfs_api(files):
    """
    Uploads a list of PDF files to the FastAPI server.
    Args:
        files (list): List of file-like objects representing PDF files.
    Returns:
        Response: The response from the FastAPI server.
    """
    files_payload = [("files", (f.name, f.read(), "application/pdf")) for f in files]
    return requests.post(f"{API_URL}/upload_pdfs/", files=files_payload)

def ask_question(question):
    return requests.post(f"{API_URL}/ask/", data={"question": question})