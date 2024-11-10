import cv2
import numpy as np
url = "http://192.168.3.42:81/stream"  # 自分のカメラの IPアドレスに変える
cam = cv2.VideoCapture(url)
if not cam.isOpened():
    print("Error: Could not open image sequence")
    exit()
while True:
    ret, img = cam.read()
    if not ret:
        print("failed to grab frame")
        break
    cv2.imshow('input image', img)
    if cv2.waitKey(30) & 0xFF == ord('q'):
        break
cam.release()
cv2.destroyAllWindows()
