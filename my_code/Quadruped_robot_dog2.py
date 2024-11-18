from xgoedu import XGOEDU
from xgolib import XGO
XGO_mini = XGO("xgomini")
XGO_edu = XGOEDU()

animal_to_audio = {
    "cat": "cat.wav",
    "bird": "bird.wav",
    "dog": "dog.wav",
    "horse": "horse.wav",
    "elephant": "elephant.wav",
    "giraffe": "giraffe.wav"
}

class robot_contrller:
    ## 初始化任务队列
    def __init__(self):
        self.command_queue = []
    
    ## 添加任务
    def add_command(self,command):
        self.command_queue.append(command)

    ## 执行任务队列
    def execute_commands(self):
        for command in self.command_queue:
            command.execute()
        self.command_queue.clear()   ## 清空任务队列

## 识别二维码
class recognize_QRcode(command):
    def execute(self):
        qr_result = XGO_edu.QRRecognition()
        if qr_result:
            print("QR Code Recognized:", qr_result)
        else:
            print("No QR Code Found")


## 识别动物并播报
class recognize_animal(command):
    def execute(self):       ## 可以在这里加参数
        # 循环进行摄像头识别，按c键退出
        while True:
            # 使用yoloFast方法进行物体识别
            result = XGO_edu.yoloFast(target="camera")
            print(result)

            # 检查结果是否为空
            if result is not None:
                # 获取识别结果和坐标
                yolo = result[0]  # 动物识别结果（字符串）
                x = result[1][0]  # x坐标（数值）
                y = result[1][1]  # y坐标（数值）
                # 检查是否识别出了已知的动物
                if yolo in animal_to_audio:
                    # 播放对应的音频文件
                    XGO_edu.xgoSpeaker(animal_to_audio[yolo])

## 播报声音
class broadcast_sound(command):
    def execute(self):
        XGO_edu.xgoSpeaker('cat.wav')

## 点灯
class turnon_led(command):
    def execute(self,led_color):
        print("led_color")

## 步骤1：前进
class move_step1(command):
    def execute(self):
        XGO_mini.move_x(7)
        time.sleep(2)
        XGO_mini.move_x(0)
        XGO_mini.move_x(7)
        time.sleep(1.3*2.5)
        XGO_mini.move_x(0)
        time.sleep(1)

class move_step2(command):
    def execute(self):
        XGO_mini.turn(45)
        time.sleep(2.3)
        XGO_mini.turn(0)
        time.sleep(1)
        XGO_mini.move_x(7)
        time.sleep(2)
        XGO_mini.move_x(0)
        XGO_mini.move_x(7)
        time.sleep(1.3*10+0.5)
        XGO_mini.move_x(0)
        time.sleep(1)
        XGO_mini.turn(-45)
        time.sleep(2.2)
        XGO_mini.turn(0)
        time.sleep(1)
        XGO_mini.move_x(7)
        time.sleep(2)
        XGO_mini.move_x(0)
        XGO_mini.move_x(7)
        time.sleep(1.3*4+0.5)
        XGO_mini.move_x(0)  





# 主函数
controller = robot_contrller()
controller.add_command(move_step1)  # 创建命令实例时传入参数
controller.add_command(recognize_animal)
controller.execute_commands()
controller.add_command(move_step2)
controller.add_command(recognize_animal)
controller.execute_commands()
