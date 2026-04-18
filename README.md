# 🚀 Gender & Age Range Prediction (Random Forest)

🌐 **Live Demo:**
👉 https://gender-age-detection-rf.onrender.com

🌐 **Image Dataset Link:**
https://www.kaggle.com/datasets/jangedoo/utkface-new

Download Zip and copy only from UTKFace folder images to data/raw if you want to run the model yourself.
---

## 📌 Project Overview

This is a **Computer Vision + Machine Learning** project that predicts:

* 👤 **Gender** (Male / Female)
* 🎂 **Age Range** (e.g., 1–10, 10–20, 20–30, etc.)

from a face image.

The system uses **Random Forest models** trained on face data and provides predictions through a clean web interface.

---

## 🧠 How It Works

1. User uploads an image
2. Face is detected using OpenCV
3. Image is preprocessed (grayscale, resized, flattened)
4. Features are passed into trained models:

   * Gender classifier
   * Age range classifier
5. Results are returned and displayed on the frontend

---

## 🛠️ Tech Stack

### 🔙 Backend

* **FastAPI** – API framework
* **Scikit-learn** – Random Forest models
* **OpenCV** – Face detection
* **NumPy / Pandas** – Data processing
* **Joblib** – Model saving/loading

### 🎨 Frontend

* **Jinja2 Templates** – Server-side rendering
* **Bootstrap 5** – UI styling
* **Vanilla JavaScript** – Image upload & API calls

### ☁️ Deployment

* **Render** – Hosting backend + frontend together

---

## 📂 Project Structure

```
gender-age-detection-rf/
│
├── app/                # FastAPI app
├── templates/          # HTML templates (frontend)
├── static/             # CSS, JS
├── models/             # Trained .pkl models
├── src/                # Training & preprocessing scripts
├── data/               # (ignored) dataset storage
├── requirements.txt
└── README.md
```

---

## ⚙️ Run Locally

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Prepare dataset

Place UTKFace images in:

```
data/raw/
```

Format:

```
[age]_[gender]_[race]_[timestamp].jpg
```

Example:

```
25_0_0_20170103200522151.jpg
```

---

### 3. Preprocess data

```bash
python src/preprocess.py
```

---

### 4. Train models

```bash
python src/train.py
```

---

### 5. Run the app

```bash
uvicorn app.main:app --reload
```

---

### 6. Open in browser

Frontend:

```
http://127.0.0.1:8000
```

API Docs:

```
http://127.0.0.1:8000/docs
```

---

## 📸 Features

* Upload image and preview
* Face detection using OpenCV
* Gender prediction
* Age range prediction
* Clean and responsive UI
* REST API support

---

## ⚠️ Notes

* Dataset is **not included** due to size
* Models are trained using **Random Forest (not deep learning)**
* Accuracy may vary depending on:

  * lighting conditions
  * image quality
  * face alignment

---

## 💡 Future Improvements

* Improve accuracy using CNN / deep learning
* Add confidence scores
* Support multiple faces
* Better UI/UX (drag-drop, animations)
* Model optimization for smaller size

---

## 👨‍💻 Author

**Washifur Rahman**

---

## ⭐ If you like this project

Give it a ⭐ on GitHub and feel free to contribute!
