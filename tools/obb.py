from ultralytics import YOLO

# TODO: Train test and check if rotation augmentation is working

# Load a model
model = YOLO("yolov8n-obb.pt")  # load an official model
# model = YOLO("yolov8n.pt")  # load an official model
# model = YOLO('path/to/best.pt')  # load a custom model

# Predict with the model
results = model(
    "https://ultralytics.com/images/bus.jpg", save=True
)  # predict on an image
