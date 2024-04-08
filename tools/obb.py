from ultralytics import YOLO

# TODO: Train test and check if rotation augmentation is working

# TODO: Test 1: Rotation augmentation check
# TODO: Test 2: Annotation format check

# Load a model
# model = YOLO("yolov8n-obb.pt")  # load an official model
model = YOLO("yolov8n-obb.pt")  # HACK: OD for test

# Train a model
results = model.train(cfg="ultralytics/cfg/obb.yaml")
