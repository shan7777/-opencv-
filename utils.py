import cv2
import os
import numpy as np

def queren(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

def moxing():
    return cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

def mox():
    return cv2.face.LBPHFaceRecognizer_create()

def xunlian(recognizer, faces, labels):
    labels = np.array(labels, dtype=np.int32)
    recognizer.train(faces, labels)
    recognizer.save('face_model.yml')

def baocunmx():
    recognizer = mox()
    try:
        recognizer.read('face_model.yml')
        return recognizer
    except:
        return None

def tiQu():
    queren('img-re')
    face_files = [f for f in os.listdir('img-re') if f.endswith('.jpg')]

    user_info = {}
    for file in face_files:
        
        parts = file.split('_')
        if len(parts) >= 4:
            user_id = int(parts[1])
            name = '_'.join(parts[2:-1])  
            if user_id not in user_info:
                user_info[user_id] = name
    
    sorted_users = sorted(user_info.items())
    names = [name for _, name in sorted_users]
    return names