import cv2  # 导入OpenCV库
import numpy as np  # 导入NumPy库，用于处理数据

# 创建一个可调整大小的窗口，并命名为"MyWindow"
cv2.namedWindow('MyWindow', cv2.WINDOW_NORMAL)
# 设置窗口大小为 640x480 像素
cv2.resizeWindow('MyWindow', 640, 480)

class ArucoDetect:
    def __init__(self, marker_size=0.04, K=None, D=None, name="camera"):
        self.name = name  # 相机名称
        self.cap = cv2.VideoCapture(0)  # 创建视频捕获对象，0代表默认摄像头
        self.marker_size = marker_size  # ArUco标记的大小
        if not K:  # 如果没有提供相机内参矩阵K
            self.K = np.array([[1187.75, 0, 1306.235], [0, 1190.407, 958.77], [0, 0, 1.0]])  # 使用默认的相机内参矩阵
        else:
            self.K = K  # 使用提供的相机内参矩阵
        if not D:  # 如果没有提供畸变系数D
            self.D = np.array([-0.0407, 0.035, -0.003216, 0.000452, 0.0])  # 使用默认的畸变系数
        else:
            self.D = D  # 使用提供的畸变系数

    def detect(self):
        ret, raw_frame = self.cap.read()  # 从摄像头读取一帧图像
        cv2.imshow("MyWindow", raw_frame)  # 显示原始图像
        frame = raw_frame  # 将原始图像赋值给frame变量
        b, g, r = cv2.split(raw_frame)  # 分离BGR通道
        raw_frame = cv2.merge((r, g, b))  # 将BGR通道合并，转换为RGB格式
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # 将图像转换为灰度图
        aruco_dict = cv2.aruco.Dictionary_get(cv2.aruco.DICT_ARUCO_ORIGINAL)  # 获取ArUco字典
        parameters = cv2.aruco.DetectorParameters_create()  # 创建检测参数
        corners, ids, rejectedImgPoints = cv2.aruco.detectMarkers(gray, aruco_dict, parameters=parameters)  # 检测ArUco标记

        if ids is not None:  # 如果检测到标记
            # 估计每个标记的位姿
            rvecs, tvecs, _ = cv2.aruco.estimatePoseSingleMarkers(corners, self.marker_size, self.K, self.D)
            # 可视化位姿
            for i in range(len(ids)):
                # 绘制标记的边界框和中心
                cv2.aruco.drawDetectedMarkers(raw_frame, corners)
                cv2.aruco.drawAxis(raw_frame, self.K, self.D, rvecs[i], tvecs[i], 0.1)
                id = ids[i]  # 获取标记的ID
        cv2.imshow("MyWindow", raw_frame)  # 显示处理后的图像
        cv2.waitKey(1)  # 等待1毫秒

if __name__ == '__main__':
    ad = ArucoDetect(marker_size=0.04)  # 创建ArucoDetect对象
    while True:  # 循环检测
        ad.detect()  # 调用detect方法进行检测