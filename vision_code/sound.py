from xgoedu import XGOEDU
XGO_edu = XGOEDU()
#为方便使用，音频相关文件的路径为/home/pi/xgoMusic，可在vscode中通过ssh传输文件
# 播放音频文件（需要按照赛题要求录制“此区域发现猫咪/鸟/狗/马/大象/长颈鹿的音频”）
XGO_edu.xgoSpeaker('cat.wav')