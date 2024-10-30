import time  
# 导入时间库
import xgolib
# 导入XGO库，用于控制机器人

dog = xgolib.XGO("/dev/ttyAMA0")
# 创建XGO对象，用于与机器人通信


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

ready_for_grasp()  # 准备抓取
time.sleep(10)  # 等待一段时间
grasp()  # 执行抓取

