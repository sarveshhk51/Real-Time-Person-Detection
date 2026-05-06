# 👤 Human Detection using YOLOv8

This project demonstrates **real-time human detection** using the **YOLOv8 object detection model** developed by Ultralytics.  
The system can detect people from both **live webcam streams** and **video files** while displaying bounding boxes and the total number of detected persons in each frame.

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## 📖 Project Overview

The main objective of this project is to build a simple, fast, and efficient **human detection system** using **YOLOv8** and **OpenCV**.

The application processes video frames in real-time and identifies all persons visible in the frame. Each detected person is highlighted with a bounding box and labeled accordingly. The total number of detected people is also displayed on the screen.

This project can be used as a foundation for:
- Smart surveillance systems
- Crowd monitoring applications
- Attendance systems
- AI-based monitoring solutions
- Security and safety applications

The project is lightweight, beginner-friendly, and easy to customize for advanced computer vision projects.

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## ⚙️ Technologies Used

- **Python 3** – Core programming language
- **OpenCV** – Image and video processing
- **YOLOv8 (Ultralytics)** – Deep learning object detection model
- **NumPy** – Numerical computations

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## ✨ Features

- 🔍 Real-time human detection using webcam
- 📦 Lightweight and fast YOLOv8 models
- 📊 Displays total number of detected persons
- ⚡ Smooth real-time performance
- 🛠️ Easy to customize and extend
- ✅ Beginner-friendly implementation

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## 📂 Project Structure

├── person_webcam.py

├── yolov8n.pt

├── requirements.txt

└── README.md

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/your-username/Human-Detection.git
cd Human-Detection
```

Install all required dependencies:

```bash
pip install -r requirements.txt
```

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## ▶️ Usage

After installing the dependencies, you can run the project.

### 🎥 Webcam Detection

Run real-time human detection using your webcam:

```bash
python person_webcam.py
```

### ⏹️ Exit the Program

Press `q` anytime to stop detection and close the application window.

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## 📊 Output

- Detects all persons visible in each frame
- Draws bounding boxes around detected humans
- Displays total number of detected persons
- Supports both webcams
- Provides smooth real-time detection performance

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## 🧠 Model Used

This project uses the **YOLOv8n** model for fast and efficient real-time object detection.

Other YOLOv8 variants can also be used depending on accuracy and performance requirements:

- `yolov8s.pt`
- `yolov8m.pt`
- `yolov8l.pt`

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## 📚 References

- https://docs.ultralytics.com/tasks/detect/

- https://opencv.org/

- https://thedatafrog.com/en/articles/human-detection-video/

