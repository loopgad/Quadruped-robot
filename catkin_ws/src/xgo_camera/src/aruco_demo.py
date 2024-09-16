import cv2
import numpy as np 


cv2.namedWindow('MyWindow', cv2.WINDOW_NORMAL)  # 创建一个可调整大小的窗口
cv2.resizeWindow('MyWindow', 640, 480)  # 设置窗口大小为 640x480 像素

class ArucoDetect:

    def __init__(self, marker_size=0.04, K=None, D=None, name="camera"):
        self.name = name
        self.cap = cv2.VideoCapture(0) 
        self.marker_size = marker_size
        if not K:
            self.K = np.array([[1187.75, 0, 1306.235], [0, 1190.407, 958.77], [0, 0, 1.0]])
        else:
            self.K = K
        if not D:
            self.D = np.array([-0.0407, 0.035, -0.003216, 0.000452, 0.0])
        else:
            self.D = D
	

    def detect(self):
        ret, raw_frame = self.cap.read()
        cv2.imshow("MyWindow", raw_frame)
        frame = raw_frame
        b, g, r = cv2.split(raw_frame)
        raw_frame = cv2.merge((r, g, b))
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        aruco_dict = cv2.aruco.Dictionary_get(cv2.aruco.DICT_ARUCO_ORIGINAL)
        parameters = cv2.aruco.DetectorParameters_create()
        corners, ids, rejectedImgPoints = cv2.aruco.detectMarkers(gray, aruco_dict, parameters=parameters)

        if ids is not None:
		# 估计每个标记的位姿
            rvecs, tvecs, _ = cv2.aruco.estimatePoseSingleMarkers(corners, self.marker_size, self.K, self.D)
		# 可视化位姿
            for i in range(len(ids)):
                # 绘制标记的边界框和中心
                cv2.aruco.drawDetectedMarkers(raw_frame, corners)
                cv2.aruco.drawAxis(raw_frame, self.K, self.D, rvecs[i], tvecs[i], 0.1)
                id = ids[i]
        cv2.imshow("MyWindow", raw_frame)
        cv2.waitKey(1)


if __name__ == '__main__':
    ad = ArucoDetect(marker_size=0.04)
    while True:
        ad.detect()
