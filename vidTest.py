
from ultralytics import YOLO

model='best21'
video_model = YOLO(f"./trainedModels/{model}.pt")
video_model.predict(source="./samples/vidSrc2.mp4", show=True, save = True, project="./results", name=f"{model}-video")