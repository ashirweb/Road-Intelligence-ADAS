import cv2
import time
import threading
import winsound
from modules.video_reader import VideoReader
from modules.lane_detector import LaneDetector
from modules.object_detector import ObjectDetector
from modules.ui_renderer import UIRenderer
from utils.fps_counter import FPSCounter

# Global flag to track if sound is currently playing
is_beeping = False

def play_warning_beep():
    global is_beeping
    is_beeping = True
    try:
        # Apni custom wav file play karein
        winsound.PlaySound("data/warning.wav", winsound.SND_FILENAME)
    except Exception as e:
        print(f"Sound error: {e}")
    finally:
        is_beeping = False

def main():
    # Aapka updated IP Webcam address
    video_source = "http://10.94.249.97:8080/video" 
    
    reader = VideoReader(source=video_source)
    lane_detector = LaneDetector()
    object_detector = ObjectDetector()
    ui_renderer = UIRenderer()
    fps_counter = FPSCounter()
    
    # Professional AI Sound Settings
    last_beep_time = 0
    beep_cooldown = 2.5  # 2.5 seconds ka perfect delay
    
    print("Road Intelligence System START ho gaya hai...")

    while True:
        success, frame = reader.get_frame()
        if not success:
            break
            
        # Pipeline execution
        lane_frame = lane_detector.process_frame(frame)
        detected_frame, warnings = object_detector.process_frame(lane_frame)
        
        fps = fps_counter.update()
        
        # --- UI RENDERER ---
        final_frame = ui_renderer.render(detected_frame, fps, warnings)
        
        # --- AUDIO ALERT LOGIC ---
        if warnings:
            current_time = time.time()
            if (current_time - last_beep_time > beep_cooldown) and not is_beeping:
                threading.Thread(target=play_warning_beep, daemon=True).start()
                last_beep_time = current_time
        
        cv2.imshow("Road Intelligence System - Pro", final_frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
            
    reader.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()