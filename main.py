import tkinter as tk
from tkinter import messagebox
from face_lu import jilu
from face_shibie import recognize

# 主窗口
class FaceRecognitionApp:
    def __init__(self, root):
        self.root = root
        self.root.title("人脸识别系统")
        self.root.geometry("400x200")
        self.capture_button = tk.Button(root, text="人脸录入", font=("Arial", 14), width=15, height=2, command=self.on_capture)
        self.capture_button.pack(pady=20)
        self.recognize_button = tk.Button(root, text="人脸识别", font=("Arial", 14), width=15, height=2, command=self.on_recognize)
        self.recognize_button.pack(pady=10)
    
    # 人脸录入按钮
    def on_capture(self):
        if jilu():
            messagebox.showinfo("提示", "人脸录入完成")
        else:
            messagebox.showerror("错误", "人脸录入失败")
    
    # 人脸识别按钮
    def on_recognize(self):
        if not recognize():
            messagebox.showerror("错误", "人脸识别失败")

# 主函数
if __name__ == "__main__":
    root = tk.Tk()
    app = FaceRecognitionApp(root)
    root.mainloop()