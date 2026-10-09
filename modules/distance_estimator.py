class DistanceEstimator:
    def __init__(self, known_width=2.0, focal_length=800):
        self.known_width = known_width 
        self.focal_length = focal_length

    def calculate_distance(self, pixel_width):
        if pixel_width == 0:
            return 0
        return (self.known_width * self.focal_length) / pixel_width