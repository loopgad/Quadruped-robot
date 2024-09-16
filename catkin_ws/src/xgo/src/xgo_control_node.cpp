#include <stdio.h>
#include <fcntl.h>
#include <termios.h> 
#include <unistd.h>
#include <errno.h>
#include <iostream>
#include <time.h>
#include <ros/init.h>
#include <ros/node_handle.h>
#include <xgo/xgo.h>
int main(int argc, char** argv) {
  ros::init(argc, argv, "xgo_control_node");
  ros::NodeHandle node_handle;
  ros::Rate loop_rate(500);
  XGO xgo(&node_handle);
  std::cout<<"Initalization done."<<std::endl;
  while(ros::ok()){
    ros::spinOnce();
    xgo.readState();
    loop_rate.sleep();
  }
  return 0;
}
