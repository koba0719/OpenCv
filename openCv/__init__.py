import cv2
def capture_camera(mirror=True, size=None):
    """Capture video from camera"""
    #カメラをキャプチャする
    cap = cv2.VideoCapture(0) # 0はカメラのデバイス番号

    while True:
        # retは画像を取得成功フラグ
        ret, frame = cap.read()

        #鏡のように映るか否か
        if mirror is True:
            frame = frame[:,::-1]

        # フレームをリサイズ
        # sizeは例えば(800,800)
        if size is not None and len(size) == 2:
            frame = cv2.resize(frame, size)

        # フレームを表示する
        cv2.imshow('camera capture', frame)


        k = cv2.waitKey(1)
        if k == 27:
            break

    #キャプチャを開放する
    cap.release()
    cv2.destroyAllWindows()