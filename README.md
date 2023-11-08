# Face Recognition with OpenCV 

In this project, we'll explore how to perform face recognition using OpenCV and the popular `face_recognition` library. The code is divided into two parts:

## Part 1: Real-Time Face Recognition (Webcam)
This part of the code captures real-time video from your webcam and recognizes known faces in the video stream. It's a handy tool for security applications or just for fun.

### Prerequisites
- Python 3.x
- OpenCV (cv2)
- face_recognition library
- A folder containing images of known faces

### Instructions
1. Organize known face images in the specified directory (change `known_faces_directory`).
2. Run the script.
3. It will compare detected faces with known faces and label them with names.

### Example
```python
python face_recognition_realtime.py
```

### Features
- Real-time face recognition from your webcam feed.
- Automatic recognition and labeling of known faces.

## Part 2: Static Image Face Recognition
This part of the code is designed to recognize faces in a static image. It loads an image, detects faces in it, and compares them with known faces, if any.

### Prerequisites
- Python 3.x
- OpenCV (cv2)
- face_recognition library
- A folder containing images of known faces

### Instructions
1. Organize known face images in the specified directory (change `known_faces_directory`).
2. Specify the path to the image you want to recognize (change `image_to_recognize`).
3. Run the script.
4. It will detect faces in the image and label them with names.

### Example
```python
python face_recognition_static_image.py
```

### Features
- Face recognition in a static image.
- Labeling recognized faces with names.

## Customization
You can customize these scripts by modifying the paths to known faces and the images you want to recognize.

## Author
Satvik Jalali
Enjoy experimenting with face recognition! If you encounter any issues or have ideas for improvements, feel free to contribute. Happy recognizing!
