import os
import cv2
import numpy as np
from dotenv import load_dotenv

from camera import Camera
from handler import Handler

load_dotenv()

webcam = Camera()
handler = Handler()
webcam.start(handle_frame=handler.handle_frame)
