import math
import time
import cv2
import numpy as np
import xgolib

dog = xgolib.XGO("/dev/ttyAMA0")


def adjust_x(vx, runtime):
    dog.move_x(vx)
    time.sleep(runtime)
    dog.move_x(0)


def adjust_y(vy, runtime):
    dog.move_y(vy)
    time.sleep(runtime)
    dog.move_y(0)


def adjust_yaw(vyaw, runtime):
    dog.turn(vyaw)
    time.sleep(runtime)
    dog.turn(0)


def filter_img(frame, color):
    b, g, r = cv2.split(frame)
    frame = cv2.merge((r, g, b))
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    color_lower = np.array(color[0])
    color_upper = np.array(color[1])
    mask = cv2.inRange(hsv, color_lower, color_upper)
    img_mask = cv2.bitwise_and(frame, frame, mask=mask)
    return img_mask


def detect_contours(frame):
    # CANNY_THRESH_1 = 16
    # CANNY_THRESH_2 = 120
    # edges = cv2.Canny(frame, CANNY_THRESH_1, CANNY_THRESH_2)
    edges = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    kernel = np.ones((5, 5), np.uint8)
    edges = cv2.dilate(edges, kernel, iterations=3)
    edges = cv2.erode(edges, kernel, iterations=3)
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    return contours, edges


def detect_block(contours, frame):
    flag = False
    length, width, angle, s_x, s_y = 0, 0, 0, 0, 0
    for i in range(0, len(contours)):
        if cv2.contourArea(contours[i]) < 20000:  #
            continue
        rect = cv2.minAreaRect(contours[i])
        # if 0.44 < rect[1][0] / rect[1][1] < 2.5:  #
        #     continue
        if not flag:
            if rect[2] > 45:
                length = rect[1][0]
                width = rect[1][1]
                angle = rect[2]
            else:
                length = rect[1][1]
                width = rect[1][0]
                angle = rect[2]
            s_x = rect[0][1]  # s_代表屏幕坐标系
            s_y = rect[0][0]
            flag = True
            box = cv2.boxPoints(rect)
            box = np.int0(box)
            # 绘制最小外接矩形
            cv2.drawContours(frame, [box], 0, (0, 255, 0), 5)
        else:  # 识别出两个及以上的矩形退出
            flag = False
            break
    return flag, length, width, angle, s_x, s_y, frame


def ready_for_grasp():
    dog.reset()
    dog.attitude("p", 15)
    time.sleep(0.5)


def grasp():
    dog.claw(0)
    dog.translation("x", 20)
    dog.motor(52, -55)
    time.sleep(0.5)
    dog.translation("z", 60)
    time.sleep(0.5)
    dog.motor(53, 80)
    dog.attitude("p", 20)
    time.sleep(2)
    dog.claw(255)
    time.sleep(2)
    dog.reset()
    time.sleep(10)


def adjust(m_angle, m_x, m_y, des_x=1050, des_y=960):
    dog.gait_type("slow_trot")
    err_x = des_x - m_x
    err_y = des_y - m_y
    print(err_y, err_x)
    if abs(err_y) < 70:
        if abs(err_x) < 50:
            grasp()
            return True
        else:
            dog.translation("x", -10)
            adjust_x(math.copysign(20, err_x), max(0.5, min(abs(err_x) / 100, 1.2)))
            dog.translation("x", 0)
    else:
        adjust_y(math.copysign(15, err_y), max(0.35, min(abs(err_y) / 200, 0.8)))
    time.sleep(0.3)
    return False


cap = cv2.VideoCapture(0)
# cv2.namedWindow("fig", cv2.WINDOW_NORMAL)
min_red = [145, 100, 70]
max_red = [185, 255, 245]
m_angle, m_x, m_y = 0, 0, 0
count = 0
COUNT_MAX = 10
ready_for_grasp()
while 1:
    # get a frame
    ret, frame = cap.read()
    frame = cv2.resize(frame, (1920, 1440))
    frame_filter = filter_img(frame, [min_red, max_red])
    counters, frame = detect_contours(frame_filter)
    flag, length, width, angle, s_x, s_y, frame = detect_block(counters, frame_filter)
    if flag:
        count += 1
        m_angle = (count - 1) / count * m_angle + angle / count
        m_x = (count - 1) / count * m_x + s_x / count
        m_y = (count - 1) / count * m_y + s_y / count
    # cv2.imshow("fig", frame)
    if count == COUNT_MAX:
        count = 0
        res = adjust(m_angle, m_x, m_y)
        if res:
            dog.claw(0)
            break

cap.release()
cv2.destroyAllWindows()
