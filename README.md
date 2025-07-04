# 📟 Image-Based Receipt Scanner & Expense Logger

This project is a simple Python-based OCR tool that extracts key information like **vendor name**, **date**, and **total amount** from a receipt image and logs the result into a CSV file in a **vertical format**.

---

## 📸 Features

* ✅ Extracts text from receipt images using Tesseract OCR
* ✅ Identifies:

  * Vendor Name
  * Purchase Date
  * Total Amount
* ✅ Saves data in vertical log style in `expenses.csv`
* ✅ Easy to modify or extend for GUI or web app

---

## 🧀 How It Works

1. You pass a **receipt image** to the program.
2. It uses **OpenCV** to preprocess the image.
3. It uses **Pytesseract** to extract text (OCR).
4. It uses **regex** to find vendor, date, and total.
5. It appends the extracted info into `expenses.csv` like:

```
vendor - ABC Store  
date - 01/07/2025  
total - 89.99  
[Full OCR Text Here]
```

---

## 💪 Installation

1. Clone the repo:

```bash
git clone https://github.com/yourusername/Image-Based-Receipt-Scanner.git
cd Image-Based-Receipt-Scanner
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Install [Tesseract-OCR](https://github.com/UB-Mannheim/tesseract/wiki) and note the install path (default is usually `C:\Program Files\Tesseract-OCR\tesseract.exe`).

---

## ⚙️ Usage

1. Open `main.py`
2. Change the image path in:

```python
img_path = r'C:\your\receipt\path.jpg'
```

3. Run:

```bash
python main.py
```

---

## 📟 Sample Output in Terminal

```
=== OCR Extracted Text ===
ABC Mart
Date: 01/07/2025
Milk - $3.00
Total: $3.00

=== Extracted Details ===
{'Vendor': 'ABC Mart', 'Date': '01/07/2025', 'Total': '3.00'}

👍 Saved in vertical format to 'expenses.csv'
```

---

## 📂 File Structure

```
Image-Based-Receipt-Scanner/
🔽
├── main.py                # Main script
├── requirements.txt       # Required Python libraries
├── README.md              # Project details
└── expenses.csv           # Output file (autogenerated)
```

---

## ✨ Future Improvements

* GUI version using Tkinter or PyQt
* Web version using Flask
* Upload multiple receipts in batch

---

## 👨‍💻 Author

**Srijoy Mitra**
B.Tech | Electronics & Communication
RCC Institute of Information Technology

---

## 📃 License

This project is open source and free to use under the [MIT License](LICENSE).
