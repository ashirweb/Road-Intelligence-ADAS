import cv2

class UIRenderer:
    def __init__(self):
        pass

    def render(self, frame, fps, warnings):
        h, w = frame.shape[:2]
        
        # --- 1. Top Black Transparent Bar (Sleek Look) ---
        overlay = frame.copy()
        cv2.rectangle(overlay, (0, 0), (w, 40), (0, 0, 0), -1)
        cv2.addWeighted(overlay, 0.6, frame, 0.4, 0, frame)
        
        cv2.putText(frame, "Road Intelligence ADAS", (15, 25), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 1)
        cv2.putText(frame, f"FPS: {fps}", (w - 100, 25), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 255), 1)

        # --- 2. Professional Warning Sign & Borders ---
        if warnings:
            # Sirf sides par red border (Thickness: 6)
            cv2.rectangle(frame, (0, 0), (w, h), (0, 0, 255), 6)
            
            # Top center par chota aur professional Brake Warning Sign
            warning_w, warning_h = 160, 35
            top_left = ((w - warning_w) // 2, 50)
            bottom_right = ((w + warning_w) // 2, 50 + warning_h)
            
            # Red Background for sign
            cv2.rectangle(frame, top_left, bottom_right, (0, 0, 255), -1)
            # White Text
            cv2.putText(frame, "[ ! ] BRAKE", (top_left[0] + 15, top_left[1] + 25), 
                        cv2.FONT_HERSHEY_DUPLEX, 0.6, (255, 255, 255), 2)

        return frame