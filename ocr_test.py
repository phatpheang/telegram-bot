import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

image_path = r"C:\ExchangeBot\images\photo_2026-08-17_10-39-00.jpg"

text = pytesseract.image_to_string(
    Image.open(image_path),
    lang="eng"
)

print(text)