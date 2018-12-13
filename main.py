from camera import Camera
import numpy as np
import cv2

def handle_frame(frame):
    frame = frame.copy()
    frame[0:100, 0:100] = (255, 0, 0)
    r = np.random.random()

    print(r)

    return frame, r > 0.99999

webcam = Camera(src=0)

webcam.start(handle_frame=handle_frame)
