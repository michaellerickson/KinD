from PIL import Image
import pytesseract

def configure_tesseract(tesseract_path=None):
    
    # Configure Tesseract OCR engine.

    tesseract_path: Path to the Tesseract executable, if not in system path.
    return None
    
    if tesseract_path:
        pytesseract.pytesseract.tesseract_cmd = tesseract_path

    print("Tesseract OCR configured successfully.")

def test_ocr(image_path):
    
    # Test OCR functionality by performing OCR on a given image.

    image_path: Path to the image for OCR testing.
    return Extracted text
    
    # Read image
    image = Image.open(image_path)

    # Perform OCR
    text = pytesseract.image_to_string(image)

    # Print extracted text
    print(f"Extracted text from {image_path}:\n{text}")

    return text

# Example usage
# tesseract_path = 'path_to_tesseract'  # Optional, if not in system path
# configure_tesseract(tesseract_path)
# image_path = 'path_to_image.png'
# test_ocr(image_path)
