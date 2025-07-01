import cv2
import pytesseract
import re
from datetime import datetime

# === Set path to Tesseract OCR ===
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# === Preprocess the image ===
def preprocess_image(img_path):
    image = cv2.imread(img_path)
    if image is None:
        print(f"[ERROR] Could not load image from path: {img_path}")
        exit()
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)
    return thresh

# === Extract text from image ===
def extract_text(img):
    return pytesseract.image_to_string(img)

# === Extract vendor, date, total ===
def extract_details(text):
    vendor = None
    match1 = re.search(r'(?:Store|Vendor|From|Sold by)[:\-]?\s*(.+)', text, re.IGNORECASE)
    if match1:
        vendor = match1.group(1).strip()
    else:
        # Take first good non-numeric line as vendor
        lines = text.strip().split('\n')
        for line in lines:
            clean = line.strip()
            if clean and len(clean) > 3 and not re.search(r'\d', clean):
                vendor = clean
                break

    date = re.search(r'\d{1,2}[/-]\d{1,2}[/-]\d{4}', text)
    total = re.search(r'Total\s*[:\-]?\s*\$?\s*(\d+(\.\d{2})?)', text, re.IGNORECASE)

    return {
        "Vendor": vendor if vendor else "Unknown",
        "Date": date.group(0) if date else datetime.now().strftime('%d/%m/%Y'),
        "Total": total.group(1) if total else "0.00",
        "Raw Text": text.strip()
    }

# === Save in vertical format to expenses.csv ===
def save_to_vertical_csv(data, filename="expenses.csv"):
    try:
        with open(filename, mode='a') as file:
            file.write(f"vendor - {data['Vendor']}\n")
            file.write(f"date - {data['Date']}\n")
            file.write(f"total - {data['Total']}\n")
            file.write(f"{data['Raw Text']}\n\n")
        print("\n✅ Saved in vertical format to 'expenses.csv'")
    except Exception as e:
        print("Error writing to CSV:", e)

# === Main Program ===
if __name__ == "__main__":
    # ✅ Use raw string for file path to avoid errors with backslashes
    img_path = r"C:\Users\profa\OneDrive\Desktop\istockphoto-1420767944-612x612.jpg"

    processed_img = preprocess_image(img_path)
    text = extract_text(processed_img)

    print("\n=== OCR Extracted Text ===\n")
    print(text)

    details = extract_details(text)

    print("\n=== Extracted Details ===\n")
    print(details)

    save_to_vertical_csv(details)
