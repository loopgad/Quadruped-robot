import cv2
import numpy as np

# 定义颜色范围常量
COLOR_RANGES = {
    'red': ([145, 100, 70], [185, 255, 245]),
    'green': ([35, 100, 70], [85, 255, 245]),
    'blue': ([85, 100, 70], [125, 255, 245]),
}
RESIZE_DIM = (1920, 1440)


class ColorBlockDetector:
    def __init__(self):
        self.cap = cv2.VideoCapture(0)
        self.current_color = 'red'  # 默认检测红色
        self.count = 0
        self.m_angle, self.m_x, self.m_y = 0, 0, 0

    def filter_img(self, frame, color_range):
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        color_lower = np.array(color_range[0])
        color_upper = np.array(color_range[1])
        mask = cv2.inRange(hsv, color_lower, color_upper)
        img_mask = cv2.bitwise_and(frame, frame, mask=mask)
        return img_mask

    def detect_contours(self, frame):
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        kernel = np.ones((5, 5), np.uint8)
        edges = cv2.dilate(gray, kernel, iterations=3)
        edges = cv2.erode(edges, kernel, iterations=3)
        contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        return contours

    def detect_block(self, contours, frame):
        flag = False
        length, width, angle, s_x, s_y = 0, 0, 0, 0, 0

        for contour in contours:
            if cv2.contourArea(contour) < 20000:
                continue

            rect = cv2.minAreaRect(contour)
            if not flag:
                length, width, angle = (rect[1][0], rect[1][1], rect[2]) if rect[2] > 45 else (
                rect[1][1], rect[1][0], rect[2])
                s_x, s_y = rect[0][1], rect[0][0]
                flag = True

                box = cv2.boxPoints(rect).astype(np.intp)
                cv2.drawContours(frame, [box], 0, (0, 255, 0), 5)
            else:
                flag = False
                break

        return flag, length, width, angle, s_x, s_y, frame

    def update_statistics(self, flag, angle, s_x, s_y):
        if flag:
            self.count += 1
            self.m_angle = (self.count - 1) / self.count * self.m_angle + angle / self.count
            self.m_x = (self.count - 1) / self.count * self.m_x + s_x / self.count
            self.m_y = (self.count - 1) / self.count * self.m_y + s_y / self.count

    def switch_color(self, key):
        if key == ord('r'):
            self.current_color = 'red'
        elif key == ord('g'):
            self.current_color = 'green'
        elif key == ord('b'):
            self.current_color = 'blue'

    def run(self):
        if not self.cap.isOpened():
            print("无法打开摄像头")
            return

        while True:
            ret, frame = self.cap.read()
            if not ret:
                print("无法读取帧")
                break

            frame = cv2.resize(frame, RESIZE_DIM)
            frame_filter = self.filter_img(frame, COLOR_RANGES[self.current_color])
            contours = self.detect_contours(frame_filter)

            flag, length, width, angle, s_x, s_y, frame_with_boxes = self.detect_block(contours, frame_filter)
            self.update_statistics(flag, angle, s_x, s_y)

            cv2.imshow("Original Image", frame)
            cv2.imshow("Contours", frame_with_boxes)

            key = cv2.waitKey(1) & 0xFF
            if key == ord('q'):
                break
            self.switch_color(key)

        self.cap.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    detector = ColorBlockDetector()
    detector.run()
