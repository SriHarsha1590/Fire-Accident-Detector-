import cv2

def detect_fire(frame, cascade_path="fire_detection.xml"):

    fire_cascade = cv2.CascadeClassifier(cascade_path)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    fire_regions = fire_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)
    fire_detected = frame.copy()
    for (x, y, w, h) in fire_regions:
        cv2.rectangle(fire_detected, (x, y), (x + w, y + h), (0, 0, 255), 2)
    return fire_detected, fire_regions

