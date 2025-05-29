# Image-Compressor-App
# 🖼️ Django Image Compressor

A web-based image compression tool built with Django and KMeans clustering. Upload an image, compress its colors using clustering, and download the optimized version — all in your browser.

---

## 🚀 Features

- 📁 Upload image files (JPG, PNG, etc.)
- 🎨 Compress image using KMeans color clustering
- 🔍 Preview compressed image before download
- ⬇️ Download the result as a PNG
- ⏳ Loading spinner during processing
- 📸 Live image preview before upload

---

## ⚙️ Tech Stack

- **Python 3.12**
- **Django 5.2.1**
- **scikit-learn** for KMeans
- **NumPy**, **Matplotlib**, **ImageIO**
- **Bulma CSS** for clean styling
- **JavaScript** for image preview & loading spinner

---

## 📦 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/YOUR_USERNAME/image-compressor.git
   cd image-compressor



2. Set up virtual environment
bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate


3. Install dependencies
bash
pip install -r requirements.txt


3. Run migrations (if needed)
bash
python manage.py migrate

4. Start the development server
bash
python manage.py runserver

6. Open in your browser
http://127.0.0.1:8000/

