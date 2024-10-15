import cv2  # 导入OpenCV库
import numpy as np  # 导入NumPy库，用于处理数据

cap = cv2.VideoCapture(0)  # 创建视频捕获对象，0代表默认摄像头
cv2.namedWindow("fig", cv2.WINDOW_NORMAL)  # 创建一个可调整大小的窗口，并命名为"fig"

while (1):  # 无限循环，直到用户决定退出
    # 获取一帧
    ret, frame = cap.read()  # 从摄像头读取一帧图像
    b, g, r = cv2.split(frame)  # 分离BGR通道
    frame = cv2.merge((r, g, b))  # 将BGR通道合并，转换为RGB格式
    # 显示一帧
    cv2.imshow("fig", frame)  # 在窗口"fig"中显示图像
    cv2.resizeWindow("fig", 600, 450)  # 设置窗口"fig"的大小为600x450像素
    if cv2.waitKey(1) & 0xFF == ord('q'):  # 如果用户按下'q'键
        # 退出并拍照
        cv2.imwrite("takephoto2.jpg", frame)  # 将当前帧保存为图片"takephoto2.jpg"

        print("take Photo Ok")  # 打印拍照成功的信息
        break  # 退出循环

cap.release()  # 释放视频捕获对象
cv2.destroyAllWindows()  # 关闭所有OpenCV窗口