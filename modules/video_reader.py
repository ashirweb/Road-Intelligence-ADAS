import cv2
import threading

class VideoReader:
    def __init__(self, source=0):
        self.cap = cv2.VideoCapture(source)
        # Network delay ko kam karne ki koshish
        self.cap.set(cv2.CAP_PROP_BUFFERSIZE, 1) 
        
        self.success, self.frame = self.cap.read()
        self.running = True
        
        # Background thread lagatar latest frame pakarta rahega
        self.thread = threading.Thread(target=self._update, daemon=True)
        self.thread.start()

    def _update(self):
        while self.running:
            success, frame = self.cap.read()
            if success:
                self.success = success
                self.frame = frame

    def get_frame(self):
        # AI ko hamesha 0-second purana (bilkul latest) frame milega
        return self.success, self.frame

    def release(self):
        self.running = False
        self.thread.join(timeout=1.0)
        self.cap.release()