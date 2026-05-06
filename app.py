from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from ultralytics import YOLO
import cv2
import numpy as np

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

model = YOLO("yolov8n.pt")


@app.get("/")
def home():
    return {
        "status": "Railway Backend Running",
        "message": "YOLOv8 Human Detection API"
    }


@app.post("/detect")
async def detect(file: UploadFile = File(...)):

    contents = await file.read()

    np_arr = np.frombuffer(contents, np.uint8)
    frame = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)

    results = model(frame)

    person_count = 0
    phone_detected = False

    for box in results[0].boxes:
        cls = int(box.cls[0])

        # Person class
        if cls == 0:
            person_count += 1

        # Cell phone class
        if cls == 67:
            phone_detected = True

    return {
        "persons_detected": person_count,
        "phone_detected": phone_detected
    }
