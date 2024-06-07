
from ultralytics import YOLO

##16,18,20,21(best)
model='best25'
img_model = YOLO(f"./trainedModels/{model}.pt")
img_model.predict(source="./samples/imgSrc4.jpg", show=True, save = True, project="./results", name=f"{model}-photo")