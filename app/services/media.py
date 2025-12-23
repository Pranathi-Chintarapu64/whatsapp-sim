import os
import uuid
import logging

logger = logging.getLogger(__name__)

MOCK_S3_DIR = "mock_s3"

def handle_media(filename: str) -> str:
    os.makedirs(MOCK_S3_DIR, exist_ok=True)

    uploaded_path = mock_upload_to_s3(filename)

    extracted_text = mock_extract_text(uploaded_path)
    return extracted_text

def mock_upload_to_s3(filename: str) -> str:
    unique_name = f"{uuid.uuid4()}_{filename}"
    file_path = os.path.join(MOCK_S3_DIR, unique_name)
    with open(file_path, "w") as f:
        f.write("Dummy medical report content")
    logger.info(f"Media uploaded to mock S3: {file_path}")
    return file_path

def mock_extract_text(file_path: str) -> str:
    logger.info(f"Extracting text from: {file_path}")
    return (
        "Report Summary: Glucose levels are slightly low. "
        "Recommendation: Monitor diet and avoid skipping meals."
    )
