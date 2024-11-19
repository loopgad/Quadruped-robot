import socket

# 创建socket对象
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# pc的IP地址
host = '192.168.100.198'

# 设置一个端口
port = 9999

# 绑定端口
server_socket.bind((host, port))

# 设置最大连接数，超过后排队
server_socket.listen(5)

print(f"服务器启动，等待连接... {host}:{port}")

while True:
    # 建立客户端连接
    client_socket, addr = server_socket.accept()
    print(f"连接地址: {str(addr)}")

    try:
        while True:
            # 接收小于 1024 字节的数据
            data = client_socket.recv(1024)
            if not data:
                # 如果没有数据，跳出循环
                break
            # 发送数据
            client_socket.send(data)

    finally:
        # 关闭连接
        client_socket.close()
