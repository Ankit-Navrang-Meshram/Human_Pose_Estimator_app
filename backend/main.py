from fastapi import FastAPI, File, UploadFile
from fastapi.responses import Response
import mediapipe as mp
import cv2
import numpy as np
import io

app = FastAPI()

# Initialize MediaPipe Pose
mp_pose = mp.solutions.pose
pose = mp_pose.Pose(
    static_image_mode=True,
    model_complexity=1, # 0=Lite, 1=Full, 2=Heavy
    enable_segmentation=False,
    min_detection_confidence=0.5
)
mp_drawing = mp.solutions.drawing_utils

@app.get("/")
def read_root():
    return {"message": "Pose Estimation API is running"}

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    # Read image file
    contents = await file.read()
    nparr = np.frombuffer(contents, np.uint8)
    image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    # Convert BGR to RGB
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    
    # Process the image
    results = pose.process(image_rgb)

    # Draw landmarks on the image
    if results.pose_landmarks:
        mp_drawing.draw_landmarks(
            image, 
            results.pose_landmarks, 
            mp_pose.POSE_CONNECTIONS,
            mp_drawing.DrawingSpec(color=(0, 255, 0), thickness=2, circle_radius=2),
            mp_drawing.DrawingSpec(color=(0, 0, 255), thickness=2, circle_radius=2)
        )

    # Encode image back to JPEG to return to client
    _, encoded_img = cv2.imencode('.jpg', image)
    return Response(content=encoded_img.tobytes(), media_type="image/jpeg")