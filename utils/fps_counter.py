import time

class FPSCounter:
    def __init__(self):
        self.prev_time = 0

    def update(self):
        current_time = time.time()
        fps = 1 / (current_time - self.prev_time) if (current_time - self.prev_time) > 0 else 0
        self.prev_time = current_time
        return int(fps)