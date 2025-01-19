import cv2
import numpy as np
from flask import Flask, Response
app = Flask(__name__)
cap = cv2.VideoCapture(0)  
cap.set(3, 640)  
cap.set(4, 480) 
cap.set(cv2.CAP_PROP_FPS, 30) 
def detect_fire(frame):
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower_bound = np.array([0, 50, 50])
    upper_bound = np.array([20, 255, 255])
    mask = cv2.inRange(hsv, lower_bound, upper_bound)
    result = cv2.bitwise_and(frame, frame, mask=mask)
    result = cv2.addWeighted(result, 1, frame, 0.7, 0)
    return result, mask
def generate_frames():
    while True:
        success, frame = cap.read()
        if not success:
            print("Failed to capture frame.")
            break
        else:
            cv2.imshow("Captured Frame", frame)
            fire_detected, _ = detect_fire(frame)
            encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 100]
            _, buffer = cv2.imencode('.jpg', fire_detected, encode_param)
            frame = buffer.tobytes()

            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/')
def index():
    return "Welcome to the Fire Detection System! Go to /video_feed to view the video stream."

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
