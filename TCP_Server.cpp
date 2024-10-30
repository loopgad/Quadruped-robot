#include <stdio.h>                      // 标准输入输出库
#include <sys/types.h>                 // 类型定义
#include <sys/socket.h>                // 套接字库
#include <errno.h>                     // 错误号库
#include <string.h>                    // 字符串处理库
#include <stdlib.h>                    // 标准库
#include <unistd.h>                    // Unix标准函数库
#include <netinet/in.h>                // Internet地址族
#include <ctype.h>                     // 字符类型库，用于字符转换

#define MAXSIZE 1024                   // 定义最大数据长度常量
#define IP_ADDR "127.0.0.1"            // 定义服务器IP地址
#define IP_PORT 8888                   // 定义服务器端口号

int main()
{
    int i_listenfd, i_connfd;           // 监听套接字和连接套接字文件描述符
    struct sockaddr_in st_sersock;     // 定义套接字地址结构体
    char msg[MAXSIZE];                 // 定义消息缓冲区
    int nrecvSize = 0;                 // 定义接收数据大小变量

    // 创建IPv4 TCP套接字
    if ((i_listenfd = socket(AF_INET, SOCK_STREAM, 0)) < 0) {
        printf("socket Error: %s (errno: %d)\n", strerror(errno), errno);
        exit(0);
    }

    // 清空地址结构体并设置IPv4地址族、任意IP地址和指定端口号
    memset(&st_sersock, 0, sizeof(st_sersock));
    st_sersock.sin_family = AF_INET;
    st_sersock.sin_addr.s_addr = htonl(INADDR_ANY); // 监听所有网卡的指定端口
    st_sersock.sin_port = htons(IP_PORT);

    // 将套接字绑定到IP地址和端口上
    if (bind(i_listenfd, (struct sockaddr*)&st_sersock, sizeof(st_sersock)) < 0) {
        printf("bind Error: %s (errno: %d)\n", strerror(errno), errno);
        exit(0);
    }

    // 设置套接字为监听状态，允许2个客户端连接请求排队
    if (listen(i_listenfd, 2) < 0) {
        printf("listen Error: %s (errno: %d)\n", strerror(errno), errno);
        exit(0);
    }

    printf("======waiting for client's request======\n");

    // 接受客户端连接请求
    if ((i_connfd = accept(i_listenfd, (struct sockaddr*)NULL, NULL)) < 0) {
        printf("accept Error: %s (errno: %d)\n", strerror(errno), errno);
    } else {
        printf("Client[%d], welcome!\n", i_connfd);
    }

    // 循环接收客户端消息并处理
    while (1) {
        memset(msg, 0, sizeof(msg)); // 清空消息缓冲区
        // 接收客户端发送的消息
        if ((nrecvSize = read(i_connfd, msg, MAXSIZE)) < 0) {
            printf("read Error: %s (errno: %d)\n", strerror(errno), errno);
            continue;
        } else if (nrecvSize == 0) { // 客户端关闭连接
            printf("client has disconnected!\n");
            close(i_connfd);
            break;
        } else {
            printf("recvMsg:%s", msg);
            // 将接收到的消息中的小写字母转换为大写字母
            for (int i = 0; msg[i] != '\0'; i++) {
                msg[i] = toupper(msg[i]);
            }
            // 将转换后的消息发送回客户端
            if (write(i_connfd, msg, strlen(msg) + 1) < 0) {
                printf("write Error: %s (errno: %d)\n", strerror(errno), errno);
            }
        }
    }

    // 关闭连接套接字和监听套接字
    close(i_connfd);
    close(i_listenfd);

    return 0; // 程序正常退出
}