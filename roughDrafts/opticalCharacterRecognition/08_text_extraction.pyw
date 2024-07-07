from PIL import Image
import pytesseract

def extract_text(image_path, tesseract_path=None):
    
    # Extract text from an image using Tesseract OCR.

    image_path: Path to the image for text extraction.
    tesseract_path: Path to the Tesseract executable, if not in system path. Optional.
    return Extracted text
    
    # Configure Tesseract path if provided
    if tesseract_path:
        pytesseract.pytesseract.tesseract_cmd = tesseract_path

    # Read image
    image = Image.open(image_path)

    # Perform OCR
    text = pytesseract.image_to_string(image)

    return text

# Example usage
# image_path = 'path_to_image.png'
# tesseract_path = 'path_to_tesseract'  # Optional, if not in system path
# text = extract_text(image_path, tesseract_path)
# print(f"Extracted text from {image_path}:\n{text}")
