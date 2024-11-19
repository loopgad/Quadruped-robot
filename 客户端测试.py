import socket
import struct
from PIL import Image


def client_program():
    # 创建socket对象
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 服务器的IP地址和端口号
    host = '127.0.0.1'
    port = 9999

    # 连接到服务器
    client_socket.connect((host, port))

    try:
        # 打开图像文件
        image_path = '微信图片_20241119223440.jpg'  # 替换为你的图像文件路径
        image = Image.open(image_path)

        # 将图像转换为字节数据
        image_bytes = image.tobytes()

        # 发送图像大小
        image_size = len(image_bytes)
        client_socket.sendall(struct.pack('>I', image_size))

        # 发送图像数据
        client_socket.sendall(image_bytes)

        print("图像发送完成")

    finally:
        # 关闭连接
        client_socket.close()


if __name__ == '__main__':
    client_program()