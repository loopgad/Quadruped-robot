#导入xgoedu
from xgoedu import XGOEDU 
#实例化edu
XGO_edu = XGOEDU()

#循环进行摄像头识别，按c键退出
while True:
    result=XGO_edu.yoloFast(target="camera")  
    print(result)
    if result!=None:     #先加结果是否为空的判断，否则会提示下标错误
        yolo=result[0]   #获取动物识别结果（字符串）
        x=result[1][0]   #获取x坐标（数值）
        y=result[1][1]   #获取y坐标（数值）
    if XGO_edu.xgoButton("c"):   #c键按下退出循环
        break