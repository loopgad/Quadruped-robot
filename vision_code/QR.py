from xgoedu import XGOEDU
XGO_edu = XGOEDU()
# 进行二维码识别
def qr_code_recognition():
    qr_result = XGO_edu.QRRecognition()
    if qr_result:
        print("QR Code Recognized:", qr_result)
    else:
        print("No QR Code Found")

qr_code_recognition()