# ESP32を用いた人物管理システム(何やってるんですか、勉強してください)

ESP32のカメラを用いて画像処理します

## 概要

- ESP32を用いて人物をカウントし、とどまっている場合音声を出して威嚇することが出来る
主な機能は
- 画像読み込み    
- 人数カウント画像処理

## インストール方法

以下の手順でプロジェクトをローカル環境にインストールしてください。

```bash
リポジトリをクローン
git clone https://github.com/yama4936/Whatareyoudoing-Pleasestudy.git

ディレクトリに移動
cd repository

依存関係をインストール
pip install -r requirements.txt 
```

## 使い方

### Arduino IDE でコードの準備

https://www.arduino.cc/en/software

からArduinoIDE2をインストールする。

1. Arduino IDE 2 起動させ、「File」>「Preferences」に選択する。

2. 以下の行をコピーして、「Additional boards manager URLs」フィールドに貼り付ける。

https://raw.githubusercontent.com/espressif/arduino-esp32/gh-pages/package_esp32_index.json

3. ボードマネージャーを開く。「Tools」>「Board」>「Boards manager」あるいは、左隅にある 「ボード マネージャー」 アイコンをクリックする。

4. ESP32 を検索し、Espressif Systems の esp32 バージョン 3.X のインストール ボタンを押す。

5. ストリーミング Web サーバーのサンプルプログラム CameraWebServer を実行する。Arduino IDE で、「Tools」>「Board」>「ESP32」に移動し、「ESP32 Wrover Module」を選択する。

6. 「ファイル」 > 「サンプル」 >「 ESP32」 > 「カメラ」に移動し、CameraWebServer サンプルを開く。

7. 表示される CameraWebServer.ino ファイルを以下のように編集する。CAMERA_MODEL_WROVER_KIT の 「//」 を削除し、他のすべてのボード選択に// があることを確認する。

8. コードを少し下にスクロールし、ボードがネットワークに接続できるように、ssid およびpassword 変数にネットワーク認証情報を挿入する。

```
const char *ssid = "************";
const char *password = "*************";
```

9. ESP32-Wrover ボードにコードをアップロード。USB ケーブル (充電専用の USB ケーブルではコードのアップロードはできない) をボードの USB コネクタに接続し、コンピューターに接続する。

10. Arduino IDE で、「Tools」>「Port」に移動し、接続されている COM ポートを選択する。

11. 「ツール」 メニューで Board: “ESP32 Wrover Module”が表示されていることを確認し、 Partition Scheme で「HugeAPP(3MB NoOTA/1MB SPIFFS)」を選択する必要がある。
 
12. 最後に、アップロードボタンをクリックする

13. コードをアップロードした後、baud rate 115200 で Arduino IDE Serial Monitor を開く。これはCameraWebServer の setup()内で Serial.begin(115200)が登録されているためである。

14. ボードの RESET(RST)ボタンを押す。シリアル モニターに ESP32カメラ の IP アドレスが表示される。

15. ストリーミングを開始するには「Start Stream」ボタンを押し、写真を撮るには「Get Still」ボタンを押す。

### 実行方法の例

```
cd PersonCount

python http_esp.py
```


## ライセンス

このプロジェクトはMITライセンスのもとで公開されています。

