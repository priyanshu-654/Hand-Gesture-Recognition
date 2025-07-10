🖐️ HandGestureAI - Real-Time Hand Gesture Recognition with Grantha Finger Mapping

## 📖 Overview

HandGestureAI** is a real-time hand gesture recognition web application built using **Flask**, OpenCV, and MediaPipe. It detects hand gestures from webcam video, classifies them (e.g., ✋ Stop, 👊 Fist, 👍 Thumbs Up), and also displays which fingers are raised using traditional **Grantha Sanskrit** finger names.

## 🚀 Features

- ✋ Real-time webcam-based gesture recognition
- 🔠 Recognizes multiple hand gestures:
  - Stop ✋
  - Fist 👊
  - Thumbs Up 👍
  - Call Me 🤙
  - Middle Finger 🖕
- 🧠 Finger name detection using Grantha Sanskrit:
  - Angushtham (Thumb)
  - Tarjani (Index)
  - Madhyama (Middle)
  - Anamika (Ring)
  - Kanishthika (Pinky)
- 🖥️ Live stream in browser via Flask
- 🧼 Clean and intuitive interface

📷 Screenshots
![Screenshot 2025-07-10 143952](https://github.com/user-attachments/assets/8b4e0b9e-01b4-489b-848b-da03a34d36e5)
![Screenshot 2025-07-10 144027](https://github.com/user-attachments/assets/fdb6125e-e93e-4abe-96ef-baa84123ee6e)

🗂️ Folder Structure
hand-gesture-recognition/
│
├── app.py # Main Flask app
│
├── static/
│ ├── css/
│ │ └── style.css # Styling for frontend
│ └── js/
│ └── script.js # Frontend JS
│
├── templates/
│ └── index.html # Web UI
│
├── requirements.txt # Python dependencies
└── README.md # Project details

 Requirements

Install the required dependencies with:

pip install -r requirements.txt

requirements.txt includes:
Flask==2.2.2
opencv-python==4.5.5.64
mediapipe==0.9.1

🛠️ Setup Instructions
Step 1: Clone the Repository
git clone https://github.com/priyanshupandey/hand-gesture-recognition.git
cd hand-gesture-recognition
Step 2: Install Dependencies
pip install -r requirements.txt
Step 3: Run the Flask App
python app.py

View the App
Open your browser and go to:
👉 http://127.0.0.1:5000

🎬 Demo Video





🤖 How It Works

📸 Webcam Input: The app captures real-time video from the webcam.

✋ Hand Detection: MediaPipe identifies hand landmarks.

🧠 Gesture Recognition: Logic based on finger positions classifies the gesture (e.g., Fist, Call Me).

📜 Finger Name Detection: Recognized raised fingers are labeled using Grantha Sanskrit (e.g., Tarjani for Index).

🌐 Live Display: The annotated frame is streamed to a browser using Flask.

🙋‍♂️ Author
👨‍💻 Priyanshu Pandey







