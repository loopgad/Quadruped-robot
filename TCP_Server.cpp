#include <stdio.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <errno.h>
#include <string.h>
#include <stdlib.h>
#include <unistd.h>
#include <netinet/in.h>
#include <ctype.h>

#define MAXSIZE 1024
#define IP_ADDR "127.0.0.1"
#define IP_PORT 8888

int main()
{
	int i_listenfd, i_connfd;
	struct sockaddr_in st_sersock;
	char msg[MAXSIZE];
	int nrecvSize = 0;

	if((i_listenfd = socket(AF_INET, SOCK_STREAM, 0) ) < 0)	//建立socket套接字
	{
		printf("socket Error: %s (errno: %d)\n", strerror(errno), errno);
		exit(0);
	}

	memset(&st_sersock, 0, sizeof(st_sersock));
	st_sersock.sin_family = AF_INET;  //IPv4协议
	st_sersock.sin_addr.s_addr = htonl(INADDR_ANY);	//INADDR_ANY转换过来就是0.0.0.0，泛指本机的意思，也就是表示本机的所有IP，因为有些机子不止一块网卡，多网卡的情况下，这个就表示所有网卡ip地址的意思。
	st_sersock.sin_port = htons(IP_PORT);

	if(bind(i_listenfd,(struct sockaddr*)&st_sersock, sizeof(st_sersock)) < 0) //将套接字绑定IP和端口用于监听
	{
		printf("bind Error: %s (errno: %d)\n", strerror(errno), errno);
		exit(0);
	}

	if(listen(i_listenfd, 20) < 0)	//设定可同时排队的客户端最大连接个数
	{
		printf("listen Error: %s (errno: %d)\n", strerror(errno), errno);
		exit(0);
	}

	printf("======waiting for client's request======\n");
	//准备接受客户端连接
	{
		if((i_connfd = accept(i_listenfd, (struct sockaddr*)NULL, NULL)) < 0)	//阻塞等待客户端连接
		{
			printf("accept Error: %s (errno: %d)\n", strerror(errno), errno);
		//	continue;
		}	
		else
		{
			printf("Client[%d], welcome!\n", i_connfd);
		}


		while(1)	//循环 接受客户端发来的消息并作处理(小写转大写)后回写给客户端
		{
			memset(msg, 0 ,sizeof(msg));
			if((nrecvSize = read(i_connfd, msg, MAXSIZE)) < 0)
			{
				printf("accept Error: %s (errno: %d)\n", strerror(errno), errno);
				continue;
			}
			else if( nrecvSize == 0)	//read返回0代表对方已close断开连接。
			{
				printf("client has disconnected!\n");
				close(i_connfd);  //
				break;
			}
			else
			{
				printf("recvMsg:%s", msg);
				for(int i=0; msg[i] != '\0'; i++)
				{
					msg[i] = toupper(msg[i]);
				}
				if(write(i_connfd, msg, strlen(msg)+1) < 0)
				{
					printf("accept Error: %s (errno: %d)\n", strerror(errno), errno);
				}

			}
		}
	}
	close(i_connfd);
	close(i_listenfd);

	return 0;
}
