import cv2
import numpy as np

class LaneDetector:
    def __init__(self):
        pass
        
    def process_frame(self, frame):
        h, w = frame.shape[:2]
        overlay = frame.copy()
        
        # Screen ke hisaab se perfect lane design set karna
        pt1 = (int(w * 0.35), int(h * 0.65))
        pt2 = (int(w * 0.65), int(h * 0.65))
        pt3 = (int(w * 0.90), h)
        pt4 = (int(w * 0.10), h)
        
        lane_polygon = np.array([[pt1, pt2, pt3, pt4]], np.int32)
        
        # Transparent Green Lane Assist Zone
        cv2.fillPoly(overlay, lane_polygon, (0, 255, 0))
        cv2.addWeighted(overlay, 0.15, frame, 0.85, 0, frame)
        
        # Lane Boundaries (Lines)
        cv2.polylines(frame, lane_polygon, isClosed=True, color=(0, 255, 0), thickness=2)
        
        return frame