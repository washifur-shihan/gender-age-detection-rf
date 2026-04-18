import joblib
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import train_test_split

def evaluate():
    X, y_gender, y_age = joblib.load("data/processed/dataset.pkl")
    gender_model = joblib.load("models/gender_model.pkl")
    age_model = joblib.load("models/age_model.pkl")

    X_train, X_test, yg_train, yg_test, ya_train, ya_test = train_test_split(
        X, y_gender, y_age, test_size=0.2, random_state=42
    )

    gender_pred = gender_model.predict(X_test)
    age_pred = age_model.predict(X_test)

    print("Gender Accuracy:", accuracy_score(yg_test, gender_pred))
    print(classification_report(yg_test, gender_pred))

    print("Age Bucket Accuracy:", accuracy_score(ya_test, age_pred))
    print(classification_report(ya_test, age_pred))

if __name__ == "__main__":
    evaluate()
