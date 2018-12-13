import imutils
import cv2
import time
from imutils.video import VideoStream

class Camera:
    def __init__(self, src=-1, name='Front Door', width=600):
        self.src = src
        self.name = name
        self.width = width
        options = { 'src': src } if src >= 0 else { 'usePiCamera': True }
        self.vs = VideoStream(**options)


    def start_stream(self):
        self.vs.start()
        time.sleep(2)


    def loop(self, handle_frame):
        while True:
            frame = self.vs.read()
            if self.width and self.src >= 0:
                frame = imutils.resize(frame, width=self.width)

            frame, break_loop = handle_frame(frame)

            cv2.imshow(self.name, frame)
            key = cv2.waitKey(1) & 0xff

            if key == ord('q') or break_loop:
                break


    def stop_stream(self):
        self.vs.stop()
        cv2.destroyAllWindows()


    def start(self, handle_frame=(lambda x: (x, False))):
        self.start_stream()
        self.loop(handle_frame)
        self.stop_stream()

