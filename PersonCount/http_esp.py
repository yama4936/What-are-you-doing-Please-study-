from ultralytics import YOLO
import cv2
import time
import winsound

# YOLOv11モデルの読み込み
model = YOLO("yolo11n.pt")  # アップロードされたファイルのパス

# カメラ映像を読み込み
cap = cv2.VideoCapture("http://192.168.3.42:81/stream")

# 人数と追跡用のIDセット
current_person_ids = set()
person_count = 0

start_time = None  # タイマーの初期化
end_time = None

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # YOLOで物体検出を行う
    results = model(frame)
    
    # 新しいフレームの人物IDを保存するセット
    new_person_ids = set()

    # 検出結果の解析
    for box in results[0].boxes:
        if box.cls == 0:  # クラスID 0 が "person" に該当
            x1, y1, x2, y2 = map(int, box.xyxy[0].tolist()) # 座標取得
            # 各人物に一意のIDを生成（例: 座標を基に生成）
            person_id = f"{x1}-{y1}-{x2}-{y2}"
            new_person_ids.add(person_id)

    # 新しく検出された人物と見えなくなった人物を確認
    added_persons = new_person_ids - current_person_ids  # 新しく検出されたID
    removed_persons = current_person_ids - new_person_ids  # 見えなくなったID

    # カウントの増減
    person_count += len(added_persons) - len(removed_persons)
    current_person_ids = new_person_ids  # 更新
    
    # カウントが1の場合、タイマーを開始または維持
    if person_count != 0:
        end_time = None
        if start_time is None:
            start_time = time.time()  # タイマーを開始
        if time.time() - start_time >= 30:  # 30秒経過チェック
            winsound.PlaySound("勉強してください.wav", winsound.SND_FILENAME)  # 音声ファイルを再生
            start_time = None  # タイマーをリセット    
    else:
        if end_time is None:
            end_time = time.time()  # タイマーを開始
        if time.time() - end_time >= 2:
            start_time = None  # タイマーをリセット
            end_time = None
        
    # デバッグ用（画面に現在のタイマー時間とカウントを表示）
    elapsed_time = time.time() - start_time if start_time else 0
    cv2.putText(frame, f"Person Count: {person_count}, Timer: {elapsed_time:.1f}s", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)

    # 結果をフレームに描画して表示
    annotated_frame = results[0].plot()
    annotated_frame = cv2.resize(annotated_frame, (1280, 720))  # フレーム自体をリサイズ（必要に応じて）

    # ウィンドウに描画した結果を表示
    cv2.imshow("YOLO Detection", annotated_frame)

    # 'q'を押すと終了
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()