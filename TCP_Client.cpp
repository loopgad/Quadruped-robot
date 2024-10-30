#include <stdio.h>                      // 标准输入输出库
#include <sys/types.h>                 // 类型定义
#include <sys/socket.h>                // 套接字库
#include <errno.h>                     // 错误号库
#include <string.h>                    // 字符串处理库
#include <stdlib.h>                    // 标准库
#include <unistd.h>                    // Unix标准函数库
#include <netinet/in.h>                // Internet地址族
#include <signal.h>                    // 信号处理库
#include <arpa/inet.h>                 // 网络地址转换库

#define MAXSIZE 1024                   // 定义最大数据长度常量
#define IP_ADDR "127.0.0.1"            // 定义服务器IP地址
#define IP_PORT 7878                   // 定义服务器端口号

int i_sockfd = -1;                     // 定义套接字文件描述符，并初始化为-1表示未创建

// 信号捕捉函数，用于捕获Ctrl+C信号
void SigCatch(int sigNum) {
    if(i_sockfd != -1) {
        close(i_sockfd);               // 如果套接字已创建，则关闭套接字
    }
    printf("Bye~! Will Exit...\n");    // 打印退出信息
    exit(0);                           // 退出程序
}

int main() {
    struct sockaddr_in st_clnsock;     // 定义套接字地址结构体
    char msg[MAXSIZE];                 // 定义消息缓冲区
    int nrecvSize = 0;                 // 定义接收数据大小变量

    // 注册信号捕获函数，当接收到SIGINT信号时调用SigCatch函数
    signal(SIGINT, SigCatch);

    // 创建套接字，AF_INET表示IPv4，SOCK_STREAM表示TCP
    if((i_sockfd = socket(AF_INET, SOCK_STREAM, 0)) < 0) {
        printf("socket Error: %s (errno: %d)\n", strerror(errno), errno);
        exit(0);
    }

    // 清空地址结构体
    memset(&st_clnsock, 0, sizeof(st_clnsock));
    st_clnsock.sin_family = AF_INET;    // 设置地址族为IPv4
    // 将IP地址从点分十进制转换为网络字节序
    if(inet_pton(AF_INET, IP_ADDR, &st_clnsock.sin_addr) <= 0) {
        printf("inet_pton Error: %s (errno: %d)\n", strerror(errno), errno);
        exit(0);
    }
    st_clnsock.sin_port = htons(IP_PORT); // 将端口号转换为网络字节序

    // 向服务器的IP地址和端口号发起连接请求
    if(connect(i_sockfd, (struct sockaddr*)&st_clnsock, sizeof(st_clnsock)) < 0) {
        printf("connect Error: %s (errno: %d)\n", strerror(errno), errno);
        exit(0);
    }

    printf("======connect to server, sent data======\n");

    while(1) { // 无限循环，持续与服务器进行数据交换
        fgets(msg, MAXSIZE, stdin);     // 从标准输入读取数据
        printf("will send: %s", msg);     // 打印即将发送的数据
        // 向服务器发送数据
        if(write(i_sockfd, msg, MAXSIZE) < 0) {
            printf("write Error: %s (errno: %d)\n", strerror(errno), errno);
            exit(0);
        }

        memset(msg, 0, sizeof(msg));     // 清空消息缓冲区
        // 从服务器接收数据
        if((nrecvSize = read(i_sockfd, msg, MAXSIZE)) < 0) {
            printf("read Error: %s (errno: %d)\n", strerror(errno), errno);
        } else if(nrecvSize == 0) {
            printf("Service Close!\n");   // 服务器关闭连接
        } else {
            printf("Server return: %s\n", msg); // 打印从服务器接收到的数据
        }
    }
    return 0; // 程序正常退出
}