Real-Time Human Detection with YOLOv8

A simple and fast human detection system built using YOLOv8 and OpenCV.
This project detects people in real-time from a webcam or video file, draws bounding boxes around them, and displays the total person count on screen.

🚀 Features
Real-time human detection using webcam
Detect people from video files
Displays live person count
Lightweight and fast YOLOv8 models
Easy to customize and extend
Beginner-friendly project structure


🛠️ Tech Stack
Python
OpenCV
YOLOv8 (Ultralytics)
NumPy
📁 Project Structure
Human-Detection/
│
├── person_webcam.py
├── person_video.py
├── input_video.mp4
├── output_video.mp4
├── yolov8n.pt
├── requirements.txt
└── README.md


📦 Installation

Clone the repository:

git clone https://github.com/your-username/Human-Detection.git
cd Human-Detection

Install dependencies:

pip install -r requirements.txt
▶️ Run the Project
Webcam Detection

Start real-time detection using your webcam:

python person_webcam.py
Video Detection

Run detection on a video file:

python person_video.py
⌨️ Controls
Key	Action
q	Exit the program


📸 Output

The system:

Detects all persons in each frame
Draws bounding boxes around detected people
Displays total number of persons detected
🧠 Model Used

This project uses YOLOv8n, a lightweight and fast object detection model from Ultralytics.

You can also replace it with:

yolov8s.pt
yolov8m.pt
yolov8l.pt

for higher accuracy.

📚 References
Ultralytics Documentation
OpenCV Documentation
YOLOv8 Object Detection Research
🌟 Future Improvements
Phone detection
Face detection
Person tracking
Suspicious activity detection
AI-based exam proctoring
