import cv2

class Detector:
    def __init__(self):
        self.face_cascade = cv2.CascadeClassifier('haar_cascades/haarcascade_frontalface_alt2.xml')

    
    @staticmethod
    def get_gray(image):
        return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


    def detect_faces(self, image):
        gray = Detector.get_gray(image)

        return self.face_cascade.detectMultiScale(gray, 1.3, 5)


    @staticmethod
    def draw_detection(image, detection, color=(0, 255, 0), label=None):
        (x, y, w, h) = detection
        cv2.rectangle(image, (x, y), (x + w, y + h), color, 2)

        if label:
            cv2.putText(image, label, (x, y + 10), cv2.FONT_HERSHEY_SIMPLEX, 0.75, color)


    @staticmethod
    def draw_detections(image, detections, color=(0, 255, 0), label=None):
        [Detector.draw_detection(image, detection, color, label) for detection in detections]


    def detect(self, image):
        faces = self.detect_people(image)
        copy = image.copy()
        Detector.draw_detections(copy, faces)

        return copy, faces
