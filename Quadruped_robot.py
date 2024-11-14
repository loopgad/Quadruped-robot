from xgoedu import XGOEDU
XGO_edu = XGOEDU()

class command:
    def execute(self): #无需显式声明虚函数
        raise NotImplementedError("Subclasses must implement this method")

class robot_contrller:
    ## 初始化任务队列
    def __init__(self):
        self.command_queue = []
    
    ## 添加任务
    def add_command(self,command):
        self.command_queue.append(command)

    ## 执行任务队列
    def execute_commands(self):
        for i in self.command_queue:
            print(self.command_queue[i])
        for command in self.command_queue:
            command.execute()
            command.pop()
        # self.command_queue.clear()   ## 清空任务队列

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


## 点灯
class turnon_led(command):
    def execute(self):
        print("led_color")

## tcp通信
class tcp_communication(command):
    def execute(self):
        print("tcp通信")

## 抓取
class gripper(command):
    def excute(self):
        print("抓取")

##分段移动，第一段
class Move_Part1(command):
    def excute(self):
        print("第一段移动")

# 使用
controller = robot_contrller()
controller.add_command(Move_Part1)  # 创建命令实例时传入参数
controller.add_command(recognize_QRcode)
controller.add_command(recognize_animal)
controller.execute_commands()