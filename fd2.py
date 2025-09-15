import cv2
import pygame
# from pydub.playback import play
from mail import send_email
fire_cascade = cv2.CascadeClassifier('fire_detection.xml')
a=False
pygame.mixer.init()
cap = cv2.VideoCapture(0)

while(True):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    fire = fire_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=4)
    if len(fire)>0:
        for (x,y,w,h) in fire:
            cv2.rectangle(frame,(x-10,y-10),(x+w+10,y+h+10),(255,0,0),3)
        if not a:
            print("fire is detected")
            pygame.mixer.Sound("alarm.wav").play()
            a=True
            send_email()
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()


