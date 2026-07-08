# 😊 Face Detection using Python and OpenCV

![Python](https://img.shields.io/badge/Python-3.x-blue)
![OpenCV](https://img.shields.io/badge/OpenCV-Computer%20Vision-green)
![License](https://img.shields.io/badge/License-MIT-yellow)

A real-time face detection application built with **Python and OpenCV**.  
This project uses the **Haar Cascade Classifier** from OpenCV to detect human faces through a webcam and display them with live bounding boxes.

This is my first Computer Vision project, created to understand the fundamentals of image processing, camera handling, and object detection using machine learning techniques.

---

# 📌 Project Overview

The application captures live video from a webcam and processes each frame using OpenCV.

The system:

1. Captures frames from the camera
2. Converts images into grayscale
3. Uses a Haar Cascade model to detect faces
4. Draws bounding boxes around detected faces
5. Displays the number of detected faces in real time

---

# ✨ Features

✅ Real-time webcam face detection  
✅ Face bounding box visualization  
✅ Live face counter  
✅ Fast and lightweight processing  
✅ Simple Computer Vision implementation  
✅ Works on normal hardware without a GPU  

---

# 🛠️ Technologies Used

## Programming Language

- Python

## Libraries

- OpenCV
- Time module

## Computer Vision Technique

- Haar Cascade Classifier

---

# 📂 Project Structure

```
FaceDetection/
│
├── main.py
│
├── models/
│   └── haarcascade_frontalface_default.xml
│
├── README.md
│
└── requirements.txt
```

---

# ⚙️ Installation

## 1. Clone the repository

```bash
git clone https://github.com/yourusername/FaceDetection.git
```

## 2. Enter the project directory

```bash
cd FaceDetection
```

## 3. Install dependencies

```bash
pip install -r requirements.txt
```

or install OpenCV directly:

```bash
pip install opencv-python
```

---

# ▶️ Running the Project

Start the application:

```bash
python main.py
```

A webcam window will open.

The program will:

- Detect faces
- Draw green rectangles around faces
- Display the face count

To close the application:

```
Press Q
```

---

# 🧠 How It Works

## 1. Camera Input

OpenCV captures live video using:

```python
cv2.VideoCapture(0)
```

Each frame from the webcam is processed individually.

---

## 2. Image Processing

The captured frame is converted from:

```
BGR Image
      |
      ↓
Grayscale Image
```

using:

```python
cv2.cvtColor()
```

Grayscale images allow faster processing because they contain less information.

---

## 3. Face Detection

The Haar Cascade model scans the image and searches for facial patterns.

The detector analyzes:

- Edges
- Shapes
- Facial features

Detected faces return coordinates:

```
(x, y, width, height)
```

---

## 4. Face Highlighting

OpenCV draws a rectangle around detected faces:

```python
cv2.rectangle()
```

and displays labels using:

```python
cv2.putText()
```

---

# 📦 Requirements

Create a `requirements.txt` file:

```
opencv-python
```

---

# 🚀 Future Improvements

This project will be expanded into a complete AI vision assistant.

Planned features:

- [ ] Face recognition
- [ ] Identify known people
- [ ] Face database
- [ ] AI personal assistant
- [ ] Emotion detection
- [ ] Object detection
- [ ] Voice interaction
- [ ] GPU accelerated inference
- [ ] Deep learning face embeddings

---

# 🎯 Learning Goals

Through this project I learned:

- How cameras work with Python
- How OpenCV processes images
- How machine learning models detect objects
- How real-time computer vision applications are built

---

# 👨‍💻 Author

**Yehen Silva**

Computer Science / Artificial Intelligence Student

GitHub:

```
https://github.com/yourusername
```

---

# 📜 License

This project is licensed under the MIT License.

You are free to use, modify, and distribute this project.

---

# ⭐ Support

If you like this project, consider giving it a ⭐ on GitHub.
