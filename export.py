from ultralytics import YOLO

print("Model load ho raha hai...")
# Purana PyTorch model load karein
model = YOLO("yolov8n.pt")

print("ONNX mein convert ho raha hai, isme 1 se 2 minute lag sakte hain. Please wait...")
# ONNX format mein export karein
model.export(format="onnx")

print("Conversion mukammal! 'yolov8n.onnx' file aapke folder mein ban gayi hai.")