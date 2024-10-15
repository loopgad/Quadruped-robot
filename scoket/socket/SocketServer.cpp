// 包含SocketServer类的声明
#include "SocketServer.h"

// 构造函数：创建socket，绑定地址，并开始监听
SocketServer::SocketServer(int port) : port(port), server_fd(0), client_fd(0) {
    // 创建socket，类型为IPv4的TCP socket
    server_fd = socket(AF_INET, SOCK_STREAM, 0);
    // 如果创建失败，打印错误信息并退出
    if (server_fd == 0) {
        perror("socket failed");
        exit(EXIT_FAILURE);
    }
    // 初始化地址结构
    address.sin_family = AF_INET; // 地址族为IPv4
    address.sin_addr.s_addr = INADDR_ANY; // 地址为任意
    address.sin_port = htons(port); // 端口号转换为网络字节序
    // 绑定地址并监听
    bindAndListen();
}

// 绑定地址到服务器socket并开始监听
void SocketServer::bindAndListen() {
    // 绑定地址到socket
    if (bind(server_fd, (struct sockaddr*)&address, sizeof(address)) < 0) {
        perror("bind failed");
        exit(EXIT_FAILURE);
    }
    // 开始监听，允许最长3个连接排队
    if (listen(server_fd, 3) < 0) {
        perror("listen");
        exit(EXIT_FAILURE);
    }
    // 打印监听信息
    std::cout << "Listening on port " << port << "...\n";
}

// 接受客户端连接
int SocketServer::acceptClient() {
    // 获取客户端地址长度
    socklen_t addrlen = sizeof(address);
    // 接受客户端连接
    client_fd = accept(server_fd, (struct sockaddr*)&address, &addrlen);
    // 如果接受失败，打印错误信息并退出
    if (client_fd < 0) {
        perror("accept");
        exit(EXIT_FAILURE);
    }
    // 打印客户端连接信息
    std::cout << "Client connected.\n";
    return client_fd;
}

// 启动服务器，等待并接受客户端连接
void SocketServer::start() {
    // 无限循环，等待并接受客户端连接
    while (true) {
        // 接受客户端连接
        client_fd = acceptClient();
        // 处理客户端请求
        handleClient();
        // 关闭客户端socket
        close(client_fd);
    }
}

// 处理客户端请求
void SocketServer::handleClient() {
    // 初始化接收缓冲区
    char buffer[1024] = {0};
    // 读取客户端发送的数据
    read(client_fd, buffer, 1024);
    // 打印客户端发送的数据
    std::cout << "Client says: " << buffer << std::endl;
    // 将数据发送回客户端
    send(client_fd, buffer, strlen(buffer), 0);
}

// 析构函数：关闭服务器socket
SocketServer::~SocketServer() {
    // 如果服务器socket已打开，关闭它
    if (server_fd > 0) {
        close(server_fd);
    }
}
