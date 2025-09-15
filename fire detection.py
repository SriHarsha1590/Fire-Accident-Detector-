import cv2
import numpy as np
from pydub import AudioSegment
from pydub.playback import play
video=cv2.VideoCapture(0)
while True:
    ret, frame= video.read()
    frame= cv2.resize(frame,(1000, 600))
    blur=cv2.GaussianBlur(frame,(15,15),0)
    hsv=cv2.cvtColor(blur,cv2.COLOR_BGR2HSV)
    lower=[20,50,50]
    upper=[35,225,255]
    lower=np.array(lower,dtype='uint8')
    upper=np.array(upper,dtype='uint8')
    mask=cv2.inRange(hsv,lower,upper)
    output=cv2.bitwise_and(frame,hsv,mask=mask)
    n=cv2.countNonZero(mask)
    if ret == False:
        break
    cv2.imshow("Video Result", output)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    if int(n)>4000:
        psong = AudioSegment.from_wav("alarm.wav")
        play(psong)
cv2.destroyAllwindows()
cv2.release()