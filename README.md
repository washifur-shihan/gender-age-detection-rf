# Gender and Age Range Prediction using Random Forest

## Features
- Detect gender
- Predict age range
- FastAPI backend
- Easy to test in VS Code

## Run steps

### 1. Install dependencies
pip install -r requirements.txt

### 2. Prepare dataset
Put images in data/raw/

### 3. Preprocess
python src/preprocess.py

### 4. Train
python src/train.py

### 5. Run API
uvicorn app.main:app --reload

### 6. Open docs
http://127.0.0.1:8000/docs
