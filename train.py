from roboflow import Roboflow
import os
from ultralytics import YOLO

# Step 1: Download the dataset using Roboflow
rf = Roboflow(api_key="fjbHo7zvsujjr5vfLSZy")
project = rf.workspace("snr-9bfms").project("all-classes-c8wwc")
version = project.version(13)
dataset = version.download("yolov8")

# Step 2: Configure the YOLOv8 model for training
# Create a YOLOv8 model object with a small architecture
model = YOLO("yolov8s.pt")

# Set the path to the dataset
data_path = os.path.join(dataset.location, "data.yaml")

# Step 3: Train the model
# Set training parameters
epochs = 100  # Number of training epochs
batch = 16  # Batch size (corrected argument)
imgsz = 640  # Image size for training

# Train the model
model.train(
    data=data_path,
    epochs=epochs,
    batch=batch,
    imgsz=imgsz,
    name='custom_yolov8s_model'
)

# Step 4: Save the trained model
# Save the trained weights to a file
model.export(format="pt", path="./best.pt")

print("Training completed and model saved successfully.")
