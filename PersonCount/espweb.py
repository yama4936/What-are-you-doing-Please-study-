from flask import Flask, Response, redirect, url_for
import cv2
from ultralytics import YOLO

app = Flask(__name__)

model = YOLO("yolo11n.pt")
cap = cv2.VideoCapture("http://192.168.3.42:81/stream")

@app.route('/')
def index():
    # トップページアクセス時に自動的に /video_feed にリダイレクトする
    return redirect(url_for('video_feed'))

def generate_frames():
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        
        # YOLOによる検出
        results = model(frame)
        annotated_frame = results[0].plot()
        ret, buffer = cv2.imencode('.jpg', annotated_frame)
        frame = buffer.tobytes()

        # フレームをJPEG形式で返す
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)