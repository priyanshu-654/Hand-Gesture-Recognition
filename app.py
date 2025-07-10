from flask import Flask, render_template, Response
import cv2
import mediapipe as mp

app = Flask(__name__)
camera = cv2.VideoCapture(0)

mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mp_draw = mp.solutions.drawing_utils

# Grantha-style finger names
grantha_fingers = ["Angushtham (Thumb)", "Tarjani (Index)", "Madhyama (Middle)", "Anamika (Ring)", "Kanishthika (Pinky)"]

def get_gesture(hand_landmarks):
    tips_ids = [4, 8, 12, 16, 20]  # Thumb, Index, Middle, Ring, Pinky
    fingers = []

    if hand_landmarks.landmark[tips_ids[0]].x < hand_landmarks.landmark[tips_ids[0] - 1].x:
        fingers.append(1)
    else:
        fingers.append(0)

    for id in range(1, 5):
        if hand_landmarks.landmark[tips_ids[id]].y < hand_landmarks.landmark[tips_ids[id] - 2].y:
            fingers.append(1)
        else:
            fingers.append(0)

    if fingers == [1, 1, 1, 1, 1]:
        return "Stop ✋"
    elif fingers == [0, 0, 0, 0, 0]:
        return "Fist 👊"
    elif fingers == [1, 0, 0, 0, 0]:
        return "Thumbs Up 👍"
    elif fingers == [1, 0, 0, 0, 1]:
        return "Call Me 🤙"
    elif fingers == [0, 0, 1, 0, 0]:
        return "Middle Finger 🖕"
    else:
        return "Gesture Not Recognized"

def gen_frames():
    while True:
        success, frame = camera.read()
        if not success:
            break
        else:
            img_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            results = hands.process(img_rgb)

            gesture_label = ""
            active_fingers = []

            if results.multi_hand_landmarks:
                for handLms in results.multi_hand_landmarks:
                    mp_draw.draw_landmarks(frame, handLms, mp_hands.HAND_CONNECTIONS)
                    gesture_label = get_gesture(handLms)

                    # Determine which fingers are raised
                    tips_ids = [4, 8, 12, 16, 20]
                    if handLms.landmark[tips_ids[0]].x < handLms.landmark[tips_ids[0] - 1].x:
                        active_fingers.append(grantha_fingers[0])
                    for id in range(1, 5):
                        if handLms.landmark[tips_ids[id]].y < handLms.landmark[tips_ids[id] - 2].y:
                            active_fingers.append(grantha_fingers[id])

            if gesture_label:
                cv2.putText(frame, f'Gesture: {gesture_label}', (20, 50),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)

            y_offset = 90
            for finger_name in active_fingers:
                cv2.putText(frame, f'{finger_name} Active', (20, y_offset),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 0), 2)
                y_offset += 35

            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()

            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video')
def video():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == "__main__":
    app.run(debug=True)
