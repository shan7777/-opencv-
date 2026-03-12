import cv2
import os
from utils import moxing, baocunmx, tiQu

def recognize():
    names = tiQu()
    face_detector = moxing()
    recognizer = baocunmx()
    if recognizer is None:
        print("未找到训练模型，请先进行人脸录入")
        return False
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("无法打开摄像头")
        return False
    print("开始人脸识别，按ESC键退出")
    while True:
        ret, frame = cap.read()
        if not ret:
            print("无法获取图像")
            break
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_detector.detectMultiScale(gray, 1.3, 5)
        for (x, y, w, h) in faces:
            face_roi = gray[y:y+h, x:x+w]
            label, confidence = recognizer.predict(face_roi)
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
            # 检查置信度和标签是否有效
            if confidence < 100 and label < len(names):
                # 显示姓名，将下划线替换为空格
                display_name = names[label].replace('_', ' ')
                cv2.putText(frame, display_name, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
            else:
                cv2.putText(frame, "无该人脸", (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)
        cv2.imshow('Face Recognition', frame)
        if cv2.waitKey(1) == 27:
            break
    cap.release()
    cv2.destroyAllWindows()
    return True