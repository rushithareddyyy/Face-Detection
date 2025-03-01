# main_recognize_image.py
# Usage: %python main_recognize_image.py

# Import the FaceDetect class
from FaceDetect.facedetect import FaceDetect

# Initialize FaceDetect

# Set the method to recognize and provide a dictionary of known faces names and image path
facedetector = FaceDetect({'mode': 'image', 'method': 'recognize', 'known-faces': {'John': 'resources/person1.png',
                                                                                   'Jane': 'resources/person2.png'}})

try:
    # When the start method is not given an image or video path, it starts the webcam
    # For Image file: facedetector.start('<path to image file>')
    # For Video: facedetector.start('<path to video file>')
    # Press 'q' to exit
    facedetector.start('resources/people.jpg')


# FaceDetect always generates a FaceDetect Exception
except Exception as error:
    print(error)
