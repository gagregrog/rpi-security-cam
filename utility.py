import os
import cv2

def info(*args):
    print('[INFO]', *args)


def capture(image, folder, filepath):
    directory = os.path.abspath(folder)
    if not os.path.exists(folder):
        os.makedirs(directory)
    
    cv2.imwrite(filepath, image)
    info('__FILE_WRITTEN__', filepath)
