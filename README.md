# 🚗 Road Intelligence System (ADAS)

A professional, real-time Advanced Driver Assistance System (ADAS) built using Python, OpenCV, and Ultralytics YOLOv8. 

## ✨ Key Features
- **Real-Time Object Detection:** Detects cars, heavy vehicles, bikes, and pedestrians using YOLOv8.
- **ONNX Acceleration:** Model exported to `.onnx` for high-speed, lag-free CPU processing.
- **Distance Estimation:** Calculates approximate distance and issues Red "Brake" warnings if vehicles are under 5 meters.
- **Smart Logic Filtering:** Prevents double bounding boxes (e.g., overlapping person and bike are merged into one label).
- **IP Webcam Integration:** Uses a smartphone camera over a local Wi-Fi hotspot as a wireless dashcam feed.
- **Pro UI Renderer:** Clean, transparent overlays with FPS counters and color-coded bounding boxes.

## 🚀 Tech Stack
- **Language:** Python 3.11
- **Computer Vision:** OpenCV
- **AI/ML Model:** YOLOv8n (Nano) -> ONNX format
- **Threading:** Custom multi-threaded video reader to bypass Wi-Fi buffer delays.

## 💡 How to Run
1. Install dependencies: `pip install opencv-python ultralytics onnxruntime`
2. Start your IP Webcam on your phone and update the IP address in `main.py`.
3. Run the system: `python main.py`