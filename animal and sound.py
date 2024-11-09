from xgoedu import XGOEDU

# 实例化XGOEDU
XGO_edu = XGOEDU()
#为方便使用，音频相关文件的路径为/home/pi/xgoMusic，可在vscode中通过ssh传输文件
# 动物名称到音频文件的映射
animal_to_audio = {
    "cat": "cat.wav",
    "bird": "bird.wav",
    "dog": "dog.wav",
    "horse": "horse.wav",
    "elephant": "elephant.wav",
    "giraffe": "giraffe.wav"
}

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

    # 检查是否按下c键
    if XGO_edu.xgoButton("c"):
        # c键按下退出循环
        break