from xgoedu import XGOEDU
XGO_edu = XGOEDU()

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


## 识别动物       
class recognize_animal(command):
    def execute(self):       ## 可以在这里加参数
        result=XGO_edu.yoloFast(target="camera")  
        print(result)
        if result!=None:     #先加结果是否为空的判断，否则会提示下标错误
            yolo=result[0]   #获取动物识别结果（字符串）
            x=result[1][0]   #获取x坐标（数值）
            y=result[1][1]   #获取y坐标（数值）

## 播报声音
class broadcast_sound(command):
    def execute(self):
        XGO_edu.xgoSpeaker('cat.wav')

## 点灯
class turnon_led(command):
    def execute(self,led_color):
        print("led_color")

## tcp通信
class tcp_communication(command):
    def execute(self):
        print("tcp通信")

## 抓取
class  gripper(command):
    def excute(self):
        print("抓取")

# 使用
controller = robot_contrller()
controller.add_command(MoveCommand("forward", 10))  # 创建命令实例时传入参数
controller.add_command(GrabCommand("box"))
controller.add_command(AvoidObstacleCommand("wall"))
controller.execute_commands()