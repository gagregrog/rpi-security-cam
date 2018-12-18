import imutils
import cv2
import time
import platform
from imutils.video import VideoStream

from utility import info

class Camera:
    def __init__(self, src=None, name='Front Door', width=600):
        self.src = src
        self.name = name
        self.width = width
        options = None
        self.pi = False

        if src is not None:
            options = { 'src': src }
        elif platform.system() == 'Darwin':
            options = { 'src': 0 }
        else:
            options = { 'usePiCamera': True }
            self.pi = True

        self.vs = VideoStream(**options)


    def start_stream(self):
        info('__START_VIDEO_STREAM__')
        self.vs.start()
        time.sleep(3)


    def loop(self, handle_frame):
        while True:
            frame = self.vs.read()
            if self.width and not self.pi:
                frame = imutils.resize(frame, width=self.width)

            frame, break_loop = handle_frame(frame)

            cv2.imshow(self.name, frame)
            key = cv2.waitKey(1) & 0xff

            if key == ord('q') or break_loop:
                break


    def stop_stream(self):
        info('__STOP_VIDEO_STREAM__')
        self.vs.stop()
        cv2.destroyAllWindows()


    def start(self, handle_frame=(lambda x: (x, False))):
        self.start_stream()
        self.loop(handle_frame)
        self.stop_stream()
