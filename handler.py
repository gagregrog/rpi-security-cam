import os
from time import time
from datetime import datetime

from gmail import Emailer
from detector import Detector
from utility import capture, info


class Handler:
    def __init__(self, capture_debounce=5):
        self.last_capture = None
        self.emailer = Emailer()
        self.detector = Detector()
        self.capture_debounce = capture_debounce


    def handle_frame(self, frame):
        detected_image, faces = self.detector.detect(frame)
        now = time()

        if len(faces) > 0 and (self.last_capture is None or now - self.last_capture > self.capture_debounce):
            info('__PERSON_DETECTED__')
            self.last_capture = now
            date = datetime.now()
            datestring = '{}-{}-{}'.format(date.month, date.day, date.year)
            folder = os.sep.join(['photos', datestring])
            filename = '{}-{}:{}:{}.png'.format(datestring, date.hour, date.minute, date.second)
            filepath = os.path.abspath(os.sep.join([folder, filename]))
            capture(detected_image, folder, filepath)
            self.emailer.send_email(filename=filepath)

        break_loop = False

        return detected_image, break_loop
