# main_detection_webcam.py
# Usage: %python main_detection_webcam.py

# Import the FaceDetect class
from FaceDetect.facedetect import FaceDetect

# Initialize FaceDetect


# Passing settings (the default ones are being passed for comparison purposes with main.py)
facedetector = FaceDetect({'mode': 'video', 'custom': False, 'method': 'detect', 'draw': True})

try:
    # When the start method is not given an image or video path, it starts the webcam
    # For Image file: facedetector.start('<path to image file>')
    # For Video: facedetector.start('<path to video file>')
    # Press 'q' to exit
    facedetector.start()


# FaceDetect always generates a FaceDetect Exception
except Exception as error:
    print(error)
