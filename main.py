import cv2
import numpy as np

from camera import Camera
from detector import Detector

detector = Detector()

def handle_frame(frame):
    detected_image, (faces, bodies) = detector.detect(frame)

    print(len(bodies))

    if len(faces) + len(bodies) > 0:
        pass 

    return detected_image, False
    

webcam = Camera(src=0)
webcam.start(handle_frame=handle_frame)
