## for Streamlit
import pytesseract

pytesseract.pytesseract.tesseract_cmd = "/usr/bin/tesseract"

def extract_text(image):
    return pytesseract.image_to_string(image)
## Local host

# import pytesseract
# pytesseract.pytesseract.tesseract_cmd = (
#     r"C:\Program Files\Tesseract-OCR\tesseract.exe")

# def extract_text(image):
#     return pytesseract.image_to_string(image)
