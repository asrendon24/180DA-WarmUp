import numpy as np
import cv2

cap = cv2.VideoCapture('videotest.mp4')
if not cap.isOpened():
    raise IOError("Cannot open webcam")

while(True):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
