import cv2
import time
import numpy as np
import requests
#http://192.168.3.42:81/stream
url = "http://192.168.3.42"
cam = cv2.VideoCapture(url+":81/stream")
size_index = 13  # 画像サイズインデックス
try:
    requests.get(url + "/control?var=framesize&val={}".format(size_index))
except:
    print("framesize: something went wrong")
time.sleep(0.2)
quality_value = 10  # 画質値
try:
    requests.get(url + "/control?var=quality&val={}".format(quality_value))
except:
    print("quality: something went wrong")
time.sleep(0.2)
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
