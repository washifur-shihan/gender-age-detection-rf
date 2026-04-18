import joblib
from app.utils import extract_features_from_image

gender_model = joblib.load("models/gender_model.pkl")
age_model = joblib.load("models/age_model.pkl")
label_maps = joblib.load("models/label_maps.pkl")

def predict_from_bytes(image_bytes: bytes):
    features = extract_features_from_image(image_bytes)

    gender_pred = gender_model.predict(features)[0]
    age_pred = age_model.predict(features)[0]

    gender_label = label_maps["gender_map"].get(int(gender_pred), str(gender_pred))

    return {
        "gender": gender_label,
        "age_range": age_pred
    }
