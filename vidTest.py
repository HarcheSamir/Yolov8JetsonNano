
from ultralytics import YOLO

model='best27'
video_model = YOLO(f"./trainedModels/{model}.pt")
video_model.predict(
    source="./samples/vidSrc6.mp4",
    show=True,
    save=True,
    project="./results",
    name=f"{model}-video",
    conf=0.4,
    classes=[i for i in range(6) if i not in [1,3, 4, 5]]
)