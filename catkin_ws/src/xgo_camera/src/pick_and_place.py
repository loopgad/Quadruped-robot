import math  # 导入数学库
import time  # 导入时间库
import cv2  # 导入OpenCV库
import numpy as np  # 导入NumPy库
import xgolib  # 导入XGO库，用于控制机器人

dog = xgolib.XGO("/dev/ttyAMA0")  # 创建XGO对象，用于与机器人通信

# 调整机器人的x方向位置
def adjust_x(vx, runtime):
    dog.move_x(vx)  # 机器人沿x轴移动
    time.sleep(runtime)  # 等待一段时间
    dog.move_x(0)  # 停止移动

# 调整机器人的y方向位置
def adjust_y(vy, runtime):
    dog.move_y(vy)  # 机器人沿y轴移动
    time.sleep(runtime)  # 等待一段时间
    dog.move_y(0)  # 停止移动

# 调整机器人的偏航角
def adjust_yaw(vyaw, runtime):
    dog.turn(vyaw)  # 机器人转动
    time.sleep(runtime)  # 等待一段时间
    dog.turn(0)  # 停止转动

# 过滤图像，只保留特定颜色
def filter_img(frame, color):
    b, g, r = cv2.split(frame)  # 分离BGR通道
    frame = cv2.merge((r, g, b))  # 合并为RGB格式
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)  # 转换为HSV颜色空间
    color_lower = np.array(color[0])  # 定义颜色的下限
    color_upper = np.array(color[1])  # 定义颜色的上限
    mask = cv2.inRange(hsv, color_lower, color_upper)  # 创建掩码
    img_mask = cv2.bitwise_and(frame, frame, mask=mask)  # 应用掩码
    return img_mask  # 返回过滤后的图像

# 检测图像轮廓
def detect_contours(frame):
    edges = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # 转换为灰度图
    kernel = np.ones((5, 5), np.uint8)  # 定义卷积核
    edges = cv2.dilate(edges, kernel, iterations=3)  # 膨胀操作
    edges = cv2.erode(edges, kernel, iterations=3)  # 腐蚀操作
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)  # 检测轮廓
    return contours, edges  # 返回轮廓和边缘图像

# 检测轮廓是否为矩形块
def detect_block(contours, frame):
    flag = False  # 标志变量，用于判断是否检测到矩形
    length, width, angle, s_x, s_y = 0, 0, 0, 0, 0
    for i in range(0, len(contours)):  # 遍历所有轮廓
        if cv2.contourArea(contours[i]) < 20000:  # 过滤小轮廓
            continue
        rect = cv2.minAreaRect(contours[i])  # 获取最小外接矩形
        if not flag:
            if rect[2] > 45:  # 根据角度判断长宽
                length = rect[1][0]
                width = rect[1][1]
                angle = rect[2]
            else:
                length = rect[1][1]
                width = rect[1][0]
                angle = rect[2]
            s_x = rect[0][1]  # 屏幕坐标系下的x坐标
            s_y = rect[0][0]  # 屏幕坐标系下的y坐标
            flag = True  # 标记检测到矩形
            box = cv2.boxPoints(rect)  # 获取矩形的四个顶点
            box = np.int0(box)  # 转换为整数类型
            cv2.drawContours(frame, [box], 0, (0, 255, 0), 5)  # 在图像上绘制矩形
        else:  # 如果检测到两个以上的矩形则退出
            flag = False
            break
    return flag, length, width, angle, s_x, s_y, frame  # 返回检测结果和图像

# 准备抓取
def ready_for_grasp():
    dog.reset()  # 重置机器人
    dog.attitude("p", 15)  # 设置机器人姿态
    time.sleep(0.5)  # 等待一段时间

# 执行抓取
def grasp():
    dog.claw(0)  # 打开爪子
    dog.translation("x", 20)  # 机器人沿x轴移动
    dog.motor(52, -55)  # 控制电机
    time.sleep(0.5)  # 等待一段时间
    dog.translation("z", 60)  # 机器人沿z轴移动
    time.sleep(0.5)  # 等待一段时间
    dog.motor(53, 80)  # 控制电机
    dog.attitude("p", 20)  # 设置机器人姿态
    time.sleep(2)  # 等待一段时间
    dog.claw(255)  # 关闭爪子
    time.sleep(2)  # 等待一段时间
    dog.reset()  # 重置机器人
    time.sleep(10)  # 等待一段时间

# 调整机器人的位置和姿态
def adjust(m_angle, m_x, m_y, des_x=1050, des_y=960):
    dog.gait_type("slow_trot")  # 设置机器人步态
    err_x = des_x - m_x  # 计算x方向误差
    err_y = des_y - m_y  # 计算y方向误差
    print(err_y, err_x)  # 打印误差
    if abs(err_y) < 70:
        if abs(err_x) < 50:
            grasp()  # 执行抓取
            return True
        else:
            dog.translation("x", -10)  # 机器人沿x轴移动
            adjust_x(math.copysign(20, err_x), max(0.5, min(abs(err_x) / 100, 1.2)))  # 调整x方向位置
            dog.translation("x", 0)  # 停止移动
    else:
        adjust_y(math.copysign(15, err_y), max(0.35, min(abs(err_y) / 200, 0.8)))  # 调整y方向位置
    time.sleep(0.3)  # 等待一段时间
    return False  # 返回False表示没有抓取

cap = cv2.VideoCapture(0)  # 创建视频捕获对象
min_red = [145, 100, 70]  # 定义红色的下限
max_red = [185, 255, 245]  # 定义红色的上限
m_angle, m_x, m_y = 0, 0, 0  # 初始化角度和坐标
count = 0  # 初始化计数器
COUNT_MAX = 10  # 设置最大计数
ready_for_grasp()  # 准备抓取
while 1:  # 无限循环
    ret, frame = cap.read()  # 读取一帧图像
    frame = cv2.resize(frame, (1920, 1440))  # 调整图像大小
    frame_filter = filter_img(frame, [min_red, max_red])  # 过滤图像
    counters, frame = detect_contours(frame_filter)  # 检测轮廓
    flag, length, width, angle, s_x, s_y, frame = detect_block(counters, frame_filter)  # 检测矩形块
    if flag:
        count += 1  # 计数器加1
        m_angle = (count - 1) / count * m_angle + angle / count  # 更新角度
        m_x = (count - 1) / count * m_x + s_x / count  # 更新x坐标
        m_y = (count - 1) / count * m_y + s_y / count  # 更新y坐标
    if count == COUNT_MAX:  # 如果达到最大计数
        count = 0  # 重置计数器
        res = adjust(m_angle, m_x, m_y)  # 调整机器人的位置和姿态
        if res:  # 如果成功抓取
            dog.claw(0)  # 打开爪子
            break  # 退出循环

cap.release()  # 释放视频捕获对象
cv2.destroyAllWindows()  # 关闭所有OpenCV窗口