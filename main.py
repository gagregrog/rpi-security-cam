import cv2
import numpy as np

from camera import Camera
from detector import Detector

detector = Detector()

def handle_frame(frame):
    detected_image, faces = detector.detect(frame)

    if len(faces) > 0:
        pass 

    return detected_image, False

# def handle_frame(frame):
#     return frame, False
    

webcam = Camera(src=-1)
webcam.start(handle_frame=handle_frame)
