import cv2
import numpy as np
import websocket  # pip install websocket-client
# import requests
# Connect to WebSocket server
ws = websocket.WebSocket()  # create a new web socket
ws.connect("ws://192.168.4.1:80/")  # connest to the server
print("Connected to WebSocket server")
# Load cascade classifier
face_classifier = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')
LED_STATE = "OFF"

while True:
    arr = np.asarray(bytearray(ws.recv()), dtype=np.uint8)
    frame = cv2.imdecode(arr, -1)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.equalizeHist(gray)
    faces = face_classifier.detectMultiScale(gray)
    big_face = False
    H, W, _ = frame.shape
    for (x, y, w, h) in faces:
        if w > W/6 and h > H/5:
            frame = cv2.rectangle(
                frame, (x, y), (x + w, y + h), (255, 255, 0), 4)
            big_face = True

    if LED_STATE == "OFF" and big_face:
        ws.send("LED_ON")
        LED_STATE = "ON"
        print(LED_STATE)
    elif LED_STATE == "ON" and not big_face:
        ws.send("LED_OFF")
        LED_STATE = "OFF"
        print(LED_STATE)
    cv2.imshow('image', frame)
    if cv2.waitKey(30) & 0xFF == ord('q'):
        break
cv2.destroyAllWindows()
ws.close()
