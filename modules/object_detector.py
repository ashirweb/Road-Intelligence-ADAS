import cv2
from ultralytics import YOLO

class ObjectDetector:
    # ONNX model yaad hai!
    def __init__(self, model_path='yolov8n.onnx'):
        self.model = YOLO(model_path, task='detect')
        # 0: Person, 1: Bicycle, 2: Car, 3: Motorcycle, 5: Bus, 7: Truck
        self.target_classes = [0, 1, 2, 3, 5, 7]

    def process_frame(self, frame):
        # conf=0.25 wapas kar diya taake kuch bhi miss na ho (No empty screens)
        results = self.model(frame, classes=self.target_classes, conf=0.25, verbose=False, stream=True)
        warnings = False
        
        detected_items = []
        
        for r in results:
            for box in r.boxes:
                x1, y1, x2, y2 = map(int, box.xyxy[0])
                cls_id = int(box.cls[0])
                class_name = self.model.names[cls_id]
                
                detected_items.append({
                    "box": (x1, y1, x2, y2),
                    "id": cls_id,
                    "name": class_name
                })

        final_boxes = []
        
        # Filter Logic: Bike ke upar bethe banday ka box hide karo
        for item in detected_items:
            x1, y1, x2, y2 = item['box']
            c_id = item['id']
            c_name = item['name']
            
            # Agar yeh 'Person' (0) hai, toh check karo kya yeh bike par hai?
            if c_id == 0:
                person_center_x = (x1 + x2) / 2
                person_center_y = (y1 + y2) / 2
                is_on_bike = False
                
                for other_item in detected_items:
                    # Agar doosri cheez motorcycle (3) ya bicycle (1) hai
                    if other_item['id'] in [1, 3]:
                        bx1, by1, bx2, by2 = other_item['box']
                        # Agar insaan ka center point bike ke dabbe ke andar hai
                        if bx1 < person_center_x < bx2 and by1 < person_center_y < by2:
                            is_on_bike = True
                            break
                
                # Agar insaan bike par hai, toh usay skip kar do (box mat banao)
                if is_on_bike:
                    continue
            
            # Namon ko saaf aur simple karein
            display_name = c_name.capitalize()
            if c_id in [1, 3]:
                display_name = "Bike"
            elif c_id in [5, 7]:
                display_name = "Truck/Bus" # Taake Car se confusion na ho
                
            final_boxes.append({"box": (x1, y1, x2, y2), "name": display_name})

        # Ab sirf theek ki hui cheezon par box draw karein
        for item in final_boxes:
            x1, y1, x2, y2 = item['box']
            display_name = item['name']
            
            # Distance Estimation
            box_width = x2 - x1
            distance_m = round(20000 / (box_width + 1)) / 10.0

            box_color = (0, 255, 0) # Green (Safe)
            if distance_m < 5.0:
                warnings = True
                box_color = (0, 0, 255) # Red (Danger)
            
            # Box aur Label Draw karein
            cv2.rectangle(frame, (x1, y1), (x2, y2), box_color, 2)
            label = f"{display_name} {distance_m}m"
            cv2.putText(frame, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, box_color, 2)
                
        return frame, warnings