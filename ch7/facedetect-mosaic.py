import cv2, sys, re

# 入力ファイルを指定 --- (※1)
if len(sys.argv) <= 1:
    print("no input file")
    quit()
image_file = sys.argv[1] 

# 出力ファイル名
output_file = re.sub(r'\.jpg|jpeg|png$', '-mosaic.jpg', image_file)
mosaic_rate = 30 

# カスケードファイルのパスを指定
cascade_file = "haarcascade_frontalface_alt.xml"

# 画像の読み込み --- (※2)
image = cv2.imread(image_file)
image_gs = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) # グレイスケール変換

# 顔認識を実行 --- (※3)
cascade = cv2.CascadeClassifier(cascade_file)
face_list = cascade.detectMultiScale(image_gs,
    scaleFactor=1.1,
    minNeighbors=1,
    minSize=(100,100))

if len(face_list) == 0:
    print("no face")
    quit()

# 認識した部分にモザイクをかける -- (*4)
print(face_list)
color = (0, 0, 255)
for (x,y,w,h) in face_list:
    # 顔を切り抜く --- (※5)
    face_img = image[y:y+h, x:x+w]
    # 切り抜いた画像を指定倍率で縮小 --- (※6)
    face_img = cv2.resize(face_img, (w//mosaic_rate, h//mosaic_rate))
    # 縮小した画像を元のサイズに戻す --- (※7)
    face_img = cv2.resize(face_img, (w, h), 
        interpolation=cv2.INTER_AREA)
    # 元の画像に貼り付ける --- (※8)
    image[y:y+h, x:x+w] = face_img
# 描画結果をファイルに書き込む
cv2.imwrite(output_file, image)

