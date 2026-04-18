# from fastapi import FastAPI, UploadFile, File
# from fastapi.responses import JSONResponse
# from app.predict import predict_from_bytes

# app = FastAPI(title="Gender and Age Range Predictor")

# @app.get("/")
# def home():
#     return {"message": "API is running"}

# @app.post("/predict")
# async def predict(file: UploadFile = File(...)):
#     try:
#         image_bytes = await file.read()
#         result = predict_from_bytes(image_bytes)
#         return JSONResponse(content=result)
#     except Exception as e:
#         return JSONResponse(status_code=400, content={"error": str(e)})


from fastapi import FastAPI, UploadFile, File, Request
from fastapi.responses import JSONResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from app.predict import predict_from_bytes

app = FastAPI(title="Gender and Age Range Predictor")

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={}
    )


@app.get("/api/health")
def health():
    return {"message": "API is running"}


@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    try:
        image_bytes = await file.read()
        result = predict_from_bytes(image_bytes)
        return JSONResponse(content=result)
    except Exception as e:
        return JSONResponse(status_code=400, content={"error": str(e)})