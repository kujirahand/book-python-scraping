import cv2
import sys

# 入力ファイルを指定する
image_file = "./photo/face1.jpg"

# カスケードファイルのパスを指定 --- (※1)
cascade_file = "haarcascade_frontalface_alt.xml"

# 画像の読み込み --- (※2)
image = cv2.imread(image_file)
# グレースケールに変換
image_gs = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 顔認識用特徴量ファイルを読み込む --- (※3)
cascade = cv2.CascadeClassifier(cascade_file)
# 顔認識の実行
face_list = cascade.detectMultiScale(image_gs,
    scaleFactor=1.1,
    minNeighbors=1,
    minSize=(150,150))

if len(face_list) > 0:
    # 認識した部分を囲む --- (※4)
    print(face_list)
    color = (0, 0, 255)
    for face in face_list:
        x,y,w,h = face
        cv2.rectangle(image, (x,y), (x+w, y+h), color, thickness=8)
    # 描画結果をファイルに書き込む --- (※5)
    cv2.imwrite("facedetect-output.png", image)
else:
    print("no face")

