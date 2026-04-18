from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
from app.predict import predict_from_bytes

app = FastAPI(title="Gender and Age Range Predictor")

@app.get("/")
def home():
    return {"message": "API is running"}

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    try:
        image_bytes = await file.read()
        result = predict_from_bytes(image_bytes)
        return JSONResponse(content=result)
    except Exception as e:
        return JSONResponse(status_code=400, content={"error": str(e)})