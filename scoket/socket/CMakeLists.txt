cmake_minimum_required(VERSION 3.16)

project(socket LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

add_executable(socket main.cpp
    SocketServer.h
    SocketServer.cpp
    win_server.cpp
    win_client.cpp)

include(GNUInstallDirs)
install(TARGETS socket
    LIBRARY DESTINATION ${CMAKE_INSTALL_LIBDIR}
    RUNTIME DESTINATION ${CMAKE_INSTALL_BINDIR}
)


# 链接系统库
find_package(Threads REQUIRED) # 用于链接线程库

