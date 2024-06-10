
from ultralytics import YOLO

##16,18,20,21(best)
model='best27'
img_model = YOLO(f"./trainedModels/{model}.pt")
img_model.predict(
    source="./samples/imgSrc2.jpg", 
    show=True,
    save = True,
    project="./results", 
    name=f"{model}-photo",
    conf=0.2,
    classes=[i for i in range(6) if i not in [1,3, 4, 5]]
)