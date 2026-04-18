import os
import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report

def train():
    X, y_gender, y_age = joblib.load("data/processed/dataset.pkl")

    # Split same features into train/test
    X_train, X_test, yg_train, yg_test, ya_train, ya_test = train_test_split(
        X, y_gender, y_age, test_size=0.2, random_state=42
    )

    gender_model = RandomForestClassifier(
        n_estimators=100,
        random_state=42,
        n_jobs=-1
    )

    age_model = RandomForestClassifier(
        n_estimators=150,
        random_state=42,
        n_jobs=-1
    )

    gender_model.fit(X_train, yg_train)
    age_model.fit(X_train, ya_train)

    gender_pred = gender_model.predict(X_test)
    age_pred = age_model.predict(X_test)

    print("\nGender Accuracy:", accuracy_score(yg_test, gender_pred))
    print(classification_report(yg_test, gender_pred))

    print("\nAge Bucket Accuracy:", accuracy_score(ya_test, age_pred))
    print(classification_report(ya_test, age_pred))

    os.makedirs("models", exist_ok=True)
    joblib.dump(gender_model, "models/gender_model.pkl")
    joblib.dump(age_model, "models/age_model.pkl")

    label_maps = {
        "gender_map": {0: "Male", 1: "Female"}
    }
    joblib.dump(label_maps, "models/label_maps.pkl")

    print("Models saved in /models")

if __name__ == "__main__":
    train()
