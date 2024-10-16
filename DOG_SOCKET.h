#pragma once

#include <stdio.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <errno.h>
#include <string.h>
#include <stdlib.h>
#include <unistd.h>
#include <netinet/in.h>
#include <signal.h>
#include <arpa/inet.h>
#include <ctype.h>
//宏定义控制服务端和客户端声明与变量
#define __Server__
//#define __Client__

#ifdef __Server__
char RX_msg[1280];
void Socket_Server_Function();
#endif

#ifdef __Client__
char RX_msg[1280];
inline void SigCatch(int sigNum);
void Socket_Server_Function();
#endif

inline bool Server_Flag = false;
inline bool Client_Flag = false;
