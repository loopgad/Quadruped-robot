import cv2
import numpy as np

# 定义常量
MIN_RED = [145, 100, 70]  # 红色下限
MAX_RED = [185, 255, 245]  # 红色上限
RESIZE_DIM = (1920, 1440)


# 过滤指定颜色范围的图像
def filter_img(frame, color):
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    color_lower = np.array(color[0])
    color_upper = np.array(color[1])
    mask = cv2.inRange(hsv, color_lower, color_upper)
    img_mask = cv2.bitwise_and(frame, frame, mask=mask)
    return img_mask


# 检测轮廓
def detect_contours(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    kernel = np.ones((5, 5), np.uint8)
    edges = cv2.dilate(gray, kernel, iterations=3)
    edges = cv2.erode(edges, kernel, iterations=3)
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    return contours


# 检测块并绘制边框
def detect_block(contours, frame):
    # 初始化变量
    flag = False
    length, width, angle, s_x, s_y = 0, 0, 0, 0, 0

    # 遍历轮廓
    for contour in contours:
        if cv2.contourArea(contour) < 20000:  # 最小面积阈值
            continue

        rect = cv2.minAreaRect(contour)

        if not flag:
            length, width, angle = (rect[1][0], rect[1][1], rect[2]) if rect[2] > 45 else (
            rect[1][1], rect[1][0], rect[2])
            s_x, s_y = rect[0][1], rect[0][0]
            flag = True

            # 绘制最小外接矩形
            box = cv2.boxPoints(rect).astype(np.intp)  # 使用 np.intp 替代 np.int0
            cv2.drawContours(frame, [box], 0, (0, 255, 0), 5)
        else:
            flag = False
            break

    return flag, length, width, angle, s_x, s_y, frame


# 主函数
def main():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("无法打开摄像头")
        return

    count = 0
    m_angle, m_x, m_y = 0, 0, 0

    while True:
        ret, frame = cap.read()
        if not ret:
            print("无法读取帧")
            break

        frame = cv2.resize(frame, RESIZE_DIM)
        frame_filter = filter_img(frame, [MIN_RED, MAX_RED])
        contours = detect_contours(frame_filter)

        # 检测块
        flag, length, width, angle, s_x, s_y, frame_with_boxes = detect_block(contours, frame_filter)

        if flag:
            count += 1
            m_angle = (count - 1) / count * m_angle + angle / count
            m_x = (count - 1) / count * m_x + s_x / count
            m_y = (count - 1) / count * m_y + s_y / count

        # 显示原始图像和检测结果
        cv2.imshow("Original Image", frame)
        cv2.imshow("Contours", frame_with_boxes)

        # 按 'q' 键退出
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
