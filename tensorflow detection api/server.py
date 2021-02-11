import uvicorn
from fastapi import FastAPI
from fastapi import UploadFile, File
# allow request from other origin (from web browser)
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import RedirectResponse  # to redirect "/" to "/docs"
from prediction import predict, read_imagefile

app = FastAPI()

# watch: https://www.youtube.com/watch?v=kCggyi_7pHg

origins = [
    "http://127.0.0.1:5500",  # serve the website and change port to your corresponding one
    "https://127.0.0.1:5500"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

# redirect to api docs:


@app.get("/", include_in_schema=False)
async def index():
    return RedirectResponse(url="/docs")


@app.post('/api/predict')
async def predict_img(img_encoded: UploadFile = File(...)):
    extension = img_encoded.filename.split(".")[-1] in ("jpg", "jpeg", "png")
    if not extension:
        return {"error": "Image must be jpg or png format!"}

    # read the file uploaded by user:
    image = read_imagefile(await img_encoded.read())

    # make predictions:
    predictions = predict(image)

    print(predictions)
    return predictions


uvicorn.run(app, host='localhost', port=3000)
