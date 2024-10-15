#ifndef SOCKETSERVER_H
#define SOCKETSERVER_H

// 保护性包含宏，防止头文件被重复包含
#ifndef SOCKET_SERVER_H
#define SOCKET_SERVER_H

// 引入标准库和系统库
#include <sys/socket.h>  // 包含socket相关函数声明
#include <netinet/in.h>   // 提供IP协议的访问接口
#include <arpa/inet.h>    // 提供inet_addr等函数
#include <unistd.h>       // 提供read, write和close函数
#include <cstring>        // 提供memset等字符串操作函数
#include <iostream>       // 提供标准输入输出流

// 声明SocketServer类
class SocketServer {
public:
    // 构造函数，初始化服务器并监听指定端口
    SocketServer(int port);
    // 析构函数，关闭服务器socket
    ~SocketServer();

    // 启动服务器，等待并接受客户端连接
    void start();

private:
    // 服务器socket文件描述符
    int server_fd;
    // 客户端socket文件描述符
    int client_fd;
    // 地址结构，保存服务器地址信息
    struct sockaddr_in address;
    // 服务器监听的端口号
    const int port;

    // 绑定地址到服务器socket并开始监听
    void bindAndListen();
    // 接受客户端连接
    int acceptClient();
    // 处理客户端请求
    void handleClient();
};

// 结束保护性包含宏
#endif // SOCKET_SERVER_H

#endif // SOCKETSERVER_H
