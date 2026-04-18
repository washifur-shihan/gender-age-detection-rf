import os 
import cv2
import numpy as np
import joblib

IMG_SIZE = 64

# Simple OpenCV face detector
FACE_CASCADE = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)


def get_age_bucket(age: int) -> str:
    if age < 10:
        return "1-10"
    elif age < 20:
        return "10-20"
    elif age < 30:
        return "20-30"
    elif age < 40:
        return "30-40"
    elif age < 50:
        return "40-50"
    elif age < 60:
        return "50-60"
    elif age < 70:
        return "60-70"
    elif age < 80:
        return "70-80"
    else:
        return "80+"
    

def parse_filename(filename: str):
    # Example filename: 25_0_abc.jpg
    # age_gender_other.jpg
    name = os.path.splitext(filename)[0]
    parts = name.split("_")
    age = int(parts[0])
    gender = int(parts[1])  # 0=male, 1=female
    return age, gender

def detect_face(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = FACE_CASCADE.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    if len(faces) == 0:
        return None

    # take the biggest face
    x, y, w, h = sorted(faces, key=lambda f: f[2] * f[3], reverse=True)[0]
    face = gray[y:y+h, x:x+w]
    face = cv2.resize(face, (IMG_SIZE, IMG_SIZE))
    return face


def load_dataset(data_dir="data/raw"):
    X = []
    y_gender = []
    y_age = []

    for filename in os.listdir(data_dir):
        if not filename.lower().endswith((".jpg", ".jpeg", ".png")):
            continue

        try:
            age, gender = parse_filename(filename)
            age_bucket = get_age_bucket(age)

            img_path = os.path.join(data_dir, filename)
            image = cv2.imread(img_path)

            if image is None:
                continue

            face = detect_face(image)
            if face is None:
                continue

            # Flatten pixel values
            features = face.flatten() / 255.0

            X.append(features)
            y_gender.append(gender)
            y_age.append(age_bucket)

        except Exception as e:
            print(f"Skipping {filename}: {e}")

    return np.array(X), np.array(y_gender), np.array(y_age)


if __name__ == "__main__":
    X, y_gender, y_age = load_dataset("data/raw")
    os.makedirs("data/processed", exist_ok=True)
    joblib.dump((X, y_gender, y_age), "data/processed/dataset.pkl")
    print("Saved processed dataset.")
    print("X shape:", X.shape)