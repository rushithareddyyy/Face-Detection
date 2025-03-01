# main_facefeatures_image.py
# Usage: %python main_facefeatures_image.py

# Import the FaceDetect class
from FaceDetect.facedetect import FaceDetect

# Initialize FaceDetect


facedetector = FaceDetect({'mode': 'image', 'face-features': ['face']})
# you can also choose to draw particular features such as:
# 'chin', 'left_eye', 'right_eye', 'left_eyebrow', 'right_eyebrow', 'nose_bridge', 'nose_tip', 'top_lip', 'bottom_lip'

try:
    # When the start method is not given an image or video path, it starts the webcam
    # For Image file: facedetector.start('<path to image file>')
    # For Video: facedetector.start('<path to video file>')
    # Press 'q' to exit
    facedetector.start('resources/people.jpg')


# FaceDetect always generates a FaceDetect Exception
except Exception as error:
    print(error)
