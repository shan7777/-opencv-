import cv2
import os
import tkinter as tk
from tkinter import simpledialog
from utils import queren, moxing, mox, xunlian, tiQu

def jilu():
    queren('img-re')
    face_detector = moxing()
    # 打开摄像头
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("无法打开摄像头")
        return False
    face_images = []
    count = 0
    
    #获取名字
    root = tk.Tk()
    root.withdraw()  # 隐藏主窗口
    name = simpledialog.askstring("输入名字", "请输入您的名字:")
    root.destroy()
    
    # 生成用户ID
    existing_names = tiQu()
    user_id = len(existing_names)
    
    print("请看向摄像头，准备拍摄人脸图像...")
    while count < 5:
        ret, frame = cap.read()
        if not ret:
            print("无法获取图像")
            break
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_detector.detectMultiScale(gray, 1.3, 5)
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
            face_roi = gray[y:y+h, x:x+w]
            # 文件生成
            safe_name = name.replace(' ', '_') if name else f"User{user_id}"
            cv2.imwrite(f'img-re/face_{user_id}_{safe_name}_{count}.jpg', face_roi)
            face_images.append(face_roi)
            count += 1
            print(f"已拍摄 {count} 张图像")
            cv2.waitKey(10)
        cv2.imshow('Face Capture', frame)
        if cv2.waitKey(1) == 27:
            break
    cap.release()
    cv2.destroyAllWindows()
    if len(face_images) > 0:
        # 加载所有已保存的人脸图像和标签
        all_faces = []
        all_labels = []
        user_info = {}
        
        # 遍历所有图像文件
        for file in os.listdir('img-re'):
            if file.endswith('.jpg'):
                parts = file.split('_')
                if len(parts) >= 4:
                    try:
                        user_id = int(parts[1])
                        name = '_'.join(parts[2:-1])
                        user_info[user_id] = name
                        
                        img_path = os.path.join('img-re', file)
                        img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
                        if img is not None:
                            all_faces.append(img)
                            all_labels.append(user_id)
                    except:
                        pass
        
        # 重新训练模型
        recognizer = mox()
        xunlian(recognizer, all_faces, all_labels)
        print("人脸录入完成，模型训练成功")
        return True
    else:
        print("未拍摄到人脸图像")
        return False