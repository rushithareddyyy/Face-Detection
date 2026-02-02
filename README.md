# Face Detection & Recognition 🎭

Real-time face detection, facial feature recognition, and face identification in images, videos, and live webcam feeds. Perfect for security systems, attendance tracking, or your next AI project!

---

## What It Does 🎯

- **Face Detection** 👤: Find and highlight all faces in images, videos, or webcam streams
- **Facial Features** 👁️: Detect eyes, nose, mouth, and other facial landmarks
- **Face Recognition** 🔍: Identify people by comparing against known faces
- **Multiple Formats** 📁: Works with images, videos, and live webcam feeds
- **Easy API** 🔧: Simple Python class you can use in your own projects

---

## Quick Start (5 mins) 🚀

### Step 1: Install Dependencies
```bash
pip install -r requirements.txt
```

**What gets installed:**
- `opencv-python` — Computer vision library
- `numpy` — Numerical computing
- `matplotlib` — Visualization
- `scikit-learn` — Machine learning

### Step 2: Run Face Detection
```bash
python Face\ Detection/facedetect.py
```

### Step 3: Use in Your Code
```python
from FaceDetect import FaceDetect

# Initialize with image
fd = FaceDetect(source='image', image_path='photo.jpg')

# Detect faces
faces = fd.detect_faces()
print(f"Found {len(faces)} faces!")

# Recognize faces (requires known_faces folder)
identified = fd.recognize_faces(known_faces_folder='./known_people/')
for person, location in identified:
    print(f"Found {person} at {location}")
```

---

## Features ✨

### Face Detection 🎭
✅ Detect all faces in images  
✅ Real-time webcam processing  
✅ Video file processing  
✅ Mark faces with rectangles  
✅ Extract individual face crops  
✅ Confidence scores  

### Face Recognition 🔎
✅ Identify known people  
✅ Name labels on detected faces  
✅ Confidence matching  
✅ Handle multiple angles  
✅ Batch processing  

### Facial Features 👁️
✅ Eye detection  
✅ Nose detection  
✅ Mouth detection  
✅ Face landmarks  
✅ Feature drawing  

---

## How to Use 📖

### 1. Detect Faces in an Image
```bash
python Face\ Detection/facedetect.py --image photo.jpg --output detected.jpg
```

**Output:** New image with faces highlighted

### 2. Process Webcam (Live)
```bash
python Face\ Detection/facedetect.py --webcam --show-features
```

**Features:** Real-time detection with facial landmarks

### 3. Recognize Faces
```bash
python Face\ Detection/facedetect.py --webcam --recognize --known-faces ./people/
```

**Features:** Identifies people in real-time

### 4. Process Video File
```bash
python Face\ Detection/facedetect.py --video my_video.mp4 --recognize
```

**Output:** New video with faces labeled

---

## Project Structure 📁

```
Face-Detection/
├── Face\ Detection/
│   └── facedetect.py           # Main FaceDetect class
├── cascades/                   # Pre-trained detection models
├── known_faces/                # Reference images for recognition
├── resources/                  # Sample images
├── output/                     # Generated output files
└── README.md
```

---

## Code Examples 💻

### Example 1: Simple Face Detection
```python
import cv2
from FaceDetect import FaceDetect

# Load image
image = cv2.imread('photo.jpg')

# Initialize detector
fd = FaceDetect()

# Detect faces
faces = fd.detect_faces(image)

# Draw rectangles
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

# Save result
cv2.imwrite('detected_faces.jpg', image)
print(f"Found {len(faces)} faces!")
```

### Example 2: Real-time Face Recognition
```python
from FaceDetect import FaceDetect
import cv2

# Initialize
fd = FaceDetect(source='webcam')

# Start webcam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    
    # Recognize faces
    identified = fd.recognize_faces(frame, 'known_faces/')
    
    # Draw labels
    for name, (x, y, w, h) in identified:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.putText(frame, name, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)
    
    cv2.imshow('Face Recognition', frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
```

---

## Requirements 📦

```
opencv-python>=4.5.0
numpy>=1.19.0
matplotlib>=3.3.0
pillow>=8.0.0
scikit-learn>=0.24.0
scipy>=1.5.0
```

Install all:
```bash
pip install -r requirements.txt
```

---

## Tips & Tricks 💡

### Better Recognition
- Use **multiple clear photos** of each person (different angles, lighting)
- **Good lighting** improves detection significantly
- Photos should be **face-focused** (close-ups work best)
- Use at least **3-5 photos per person**

### Faster Processing
- Lower image resolution for real-time video
- Use **GPU acceleration** if available
- Process every 2nd frame instead of every frame
- **Crop regions of interest** before processing

### Better Accuracy
- Use **high-quality images**
- Ensure good **lighting conditions**
- **Clean up** known_faces folder (remove blurry/bad photos)
- Test with **multiple threshold values**

---

## Common Use Cases 🎬

✅ **Security Systems** — Door entry, surveillance  
✅ **Attendance Tracking** — Automatic classroom/office attendance  
✅ **Photo Organization** — Auto-tag people in photos  
✅ **Video Analysis** — Count people, detect crowds  
✅ **Access Control** — Secure building/room entry  
✅ **Social Media** — Auto-face blur for privacy  
✅ **Retail Analytics** — Customer counting & analysis  

---

## Troubleshooting 🔧

**Q: "No faces detected in my image"**
- Check image quality and lighting
- Try a closer/clearer photo
- Adjust detection threshold in code
- Ensure face is clearly visible

**Q: "Recognition not working"**
- Add more training images (minimum 3-5 per person)
- Use clear, well-lit photos
- Remove low-quality images from known_faces/
- Increase similarity threshold

**Q: "Slow performance"**
- Reduce video resolution
- Process fewer frames per second
- Use GPU acceleration (CUDA)
- Process only face regions

**Q: "Wrong faces detected"**
- Check cascade file is correct
- Adjust scaleFactor and minNeighbors
- Try different detection method
- Use higher resolution image

---

## Advanced Features 🚀

### Custom Cascade Classifiers
Train your own detection model:
```bash
opencv_traincascade -data cascade_data/ -vec samples.vec -bg negatives.txt -numStages 15
```

### GPU Acceleration
Enable CUDA for faster processing:
```python
cv2.cuda.setDevice(0)  # Select GPU device
```

### Multi-threaded Processing
Process multiple streams simultaneously for better performance

---

## What's Next? 🔮

### Features to Add
- [ ] Deep learning-based detection (YOLO, SSD)
- [ ] Age/gender estimation
- [ ] Emotion detection
- [ ] Face beautification filters
- [ ] Real-time video streaming
- [ ] Web interface
- [ ] Mobile app

### To Deploy
- Deploy as REST API
- Create web dashboard
- Build desktop application
- Mobile app version
- Cloud deployment

---

## License 📜

MIT License - Use freely, modify, share!

---

## Made By

**Rushitha**  
Computer Vision | AI | Open Source

Have feedback? [Open an issue](https://github.com/rushithareddyyy/Face-Detection/issues)  
Want to contribute? [Submit a PR](https://github.com/rushithareddyyy/Face-Detection/pulls)

**Last Updated:** February 2026  
**Status:** ✅ Active & Maintained
