import socket
from PIL import Image
import struct

def server_program():
    # 创建socket对象
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 服务器的IP地址和端口号
    host = '127.0.0.1'
    port = 9999

    # 绑定端口
    server_socket.bind((host, port))

    # 监听连接
    server_socket.listen(5)
    print("服务器启动，等待连接...")

    # 接受连接
    client_socket, addr = server_socket.accept()
    print(f"连接来自 {addr}")

    try:
        # 接收图像大小
        image_size_data = client_socket.recv(8)
        image_size = struct.unpack('>I', image_size_data)[0]
        print(f"接收到图像大小：{image_size} 字节")

        # 接收图像数据
        image_bytes = b''
        while len(image_bytes) < image_size:
            more_bytes = client_socket.recv(image_size - len(image_bytes))
            if not more_bytes:
                break
            image_bytes += more_bytes

        # 将接收到的字节数据转换为图像
        # 这里的尺寸需要根据实际图像尺寸调整
        image = Image.frombytes('RGB', (676, 456), image_bytes)

        # 保存图像
        image.save('received_image.jpg', 'JPEG')
        print("图像接收并保存完成")

    finally:
        # 关闭连接
        client_socket.close()
        server_socket.close()

if __name__ == '__main__':
    server_program()