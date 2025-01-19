import cv2
import time
import numpy as np
from fd import detect_fire
from alarm import play_alert_sound
from ml import send_email
cap = cv2.VideoCapture(0)

fire_alert_triggered = False

cascade_path = 'fire_detection.xml'  

while True:
    success, frame = cap.read()  
    if not success:
        break

    fire_detected, fire_regions = detect_fire(frame, cascade_path)

    if len(fire_regions) > 0 and not fire_alert_triggered:
        print("Fire detected!")
        play_alert_sound()  
        send_email(
            subject="Fire Detected",
            body="A fire has been detected in the monitored area.",
            to_email="receiver mail adress" 
        )
      
        fire_alert_triggered = True
        if fire_alert_triggered:
            cap.release()
            cv2.destroyAllWindows()    
    cv2.imshow("Fire Detection Feed", fire_detected)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
