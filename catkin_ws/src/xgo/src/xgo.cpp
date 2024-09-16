#include <stdio.h>
#include "xgo/xgo.h"
#include <stdio.h>
#include <fcntl.h>
#include <termios.h> 
#include <unistd.h>
#include <errno.h>
#include <iostream>
#include <time.h>
#include <ros/init.h>
#include <ros/node_handle.h>
#include <geometry_msgs/Twist.h>


float Saturation(float data,float min_limit,float max_limit){
    if(data<min_limit)
        return min_limit;
    else if(data>max_limit)
        return max_limit;
    else
        return data;
}

float uint82float(uint8_t data,float min_limit,float max_limit){
    return (float)data/255.0*(max_limit-min_limit)+min_limit;
}

uint8_t float2uint8(float data, float min_limit,float max_limit){    
    return (uint8_t)((data-min_limit)/(max_limit-min_limit)*255);
}

float bytes2float(uint8_t* databytes){
    return *(float*)(databytes);
}

XGO::XGO(ros::NodeHandle* nodehandle):nh_(*nodehandle){
    ROS_INFO("Initializing xgo node...");
    initParam();
    initCOM();
    initSubcriber();
    initPublisher();
}

bool XGO::initParam(){
    if(nh_.getParam("vx_max",vx_max) &&
       nh_.getParam("vy_max",vy_max) &&
       nh_.getParam("vyaw_max",vyaw_max) &&
       nh_.getParam("period_limit",period_limit) &&
       nh_.getParam("joint_limit",joint_limit_xml) &&
       nh_.getParam("arm_limit",arm_limit_xml) &&
       nh_.getParam("body_limit",body_limit_xml) &&
       nh_.getParam("enable_joint_gui",enable_joint_gui))
       {
            joint_limit.resize(joint_limit_xml.size());
            for(int i=0;i<joint_limit_xml.size();++i){
                for(int j=0;j<joint_limit_xml[i].size();++j){
                    joint_limit[i].push_back(static_cast<int>(joint_limit_xml[i][j]));
                }
            }

            arm_limit.resize(arm_limit_xml.size());
            for(int i=0;i<arm_limit_xml.size();++i){
                for(int j=0;j<arm_limit_xml[i].size();++j){
                    arm_limit[i].push_back(static_cast<int>(arm_limit_xml[i][j]));
                }
            }

            body_limit.resize(body_limit_xml.size());
            for(int i=0;i<body_limit_xml.size();++i){
                for(int j=0;j<body_limit_xml[i].size();++j){
                    body_limit[i].push_back(static_cast<int>(body_limit_xml[i][j]));
                }
            }
            return true;
       }else{
            ROS_ERROR("Initializing param failed!");
            return false;
       }

}

bool XGO::initCOM(){
    if(nh_.getParam("com_port",com_port_str)){
        std::cout<<"Connecting to "<<com_port_str<<std::endl;
    }
    std::strcpy(com_port,com_port_str.c_str());
    serial::Timeout to = serial::Timeout::simpleTimeout(100);
    ser.setPort(com_port_str);
    ser.setBaudrate(115200);
    ser.setTimeout(to);
    ser.open();
    sendOrder(0x08,0x01);
    sendOrder(0x08,0x01);
    return true;
}

void XGO::initSubcriber(){
    sub_cmd_vel_ = nh_.subscribe("/cmd_vel",10,     &XGO::cmdvelCallback, this);
    sub_body_pose_ = nh_.subscribe("/body_pose",10, &XGO::bodyposeCallback, this);
    sub_arm_pose_ = nh_.subscribe("/arm_pose",10,   &XGO::armposeCallback, this);
    sub_joint_angle_ = nh_.subscribe("/joint_angle",10, &XGO::jointangleCallback, this);
    sub_leg_pose_ = nh_.subscribe("/leg_pose",10,       &XGO::legposeCallback, this);
    sub_order_ = nh_.subscribe("/order",10,       &XGO::orderCallback, this);
}

void XGO::initPublisher(){
    if(!enable_joint_gui){
        pub_joint_ = nh_.advertise<sensor_msgs::JointState>("/joint_states",10);
    }
}

void XGO::readState(){
    int readLen = ser.available();

    uint8_t tempPtr = 0;
    if(readLen>0){
        readLen = ser.read(rxBuffer,readLen);
        while(tempPtr!=readLen){
            switch(rxFlag){
                case 0:
                    if(rxBuffer[tempPtr]==0x55)
                        rxFlag = 1;
                    break;
                case 1:
                    if(rxBuffer[tempPtr]==0x00)
                        rxFlag = 2;
                    else
                        rxFlag = 0;
                    break;
                case 2:
                    rxData[rxPtr++] = rxBuffer[tempPtr];
                    if(rxPtr==40){
                        rxFlag = 3;
                    }
                    break;
                case 3:
                    if(rxBuffer[tempPtr]==0x00)
                        rxFlag = 4;
                    else
                        rxFlag = 0;
                    break;
                case 4:
                    if(rxBuffer[tempPtr]==0xAA)
                        updateState();
                    rxFlag = 0;
                    rxPtr = 0;
                    break;
                default:
                    rxFlag = 0;
                    rxPtr = 0;
                    break;
            }
            tempPtr++;
        }
    }
}

void XGO::updateState(){
    battery = rxData[0];
    for(int i=0;i<15;i++){
        if(i<12){
            joint_angle[i] = uint82float(rxData[1+i],joint_limit[i%3][0],joint_limit[i%3][1])/57.3;
        }else{
            joint_angle[i] = uint82float(rxData[1+i],joint_limit[i-9][0],joint_limit[i-9][1])/57.3;
        }
    }
    imu_angle[0] = bytes2float(rxData+16)/57.3;
    imu_angle[1] = bytes2float(rxData+20)/57.3;
    imu_angle[2] = bytes2float(rxData+24)/57.3;
    imu_acc[0] = bytes2float(rxData+28);
    imu_acc[1] = bytes2float(rxData+32);
    imu_acc[2] = bytes2float(rxData+36);
    pubJointState();
    pubBaseTf();
}

void XGO::cmdvelCallback(const geometry_msgs::Twist& msg){
     vx = Saturation(msg.linear.x,-vx_max,vx_max);
     vy = Saturation(msg.linear.y,-vy_max,vy_max);
     vyaw = Saturation(msg.angular.z,-vyaw_max,vyaw_max);
     sendSpeed();
}

void XGO::jointangleCallback(const std_msgs::Float32MultiArray& msg){
    // motor11 motor12 motor13 motor21 .. motor51 motor52 motor53
    for(int i=0;i<15;i++){
        joint_angle[i] = msg.data[i];
        sendMotorAngle();
    }
}

void XGO::bodyposeCallback(const std_msgs::Float32MultiArray& msg){
    // x y z roll pitch yaw
    for(int i=0;i<6;i++){ 
        body_pose[i] = msg.data[i];
        sendBodyPose();
    }   
}

void XGO::legposeCallback(const std_msgs::Float32MultiArray& msg){
    // leg1_x leg1_y leg1_z  leg2_x leg2_y leg2_z ... 
    for(int i=0;i<12;i++){
        leg_pose[i] = msg.data[i];
        sendLegPose();
    }   
}

void XGO::armposeCallback(const std_msgs::Float32MultiArray& msg){
    // claw(0-100) arm_x arm_z
    for(int i=0;i<3;i++){
        arm_pose[i] = msg.data[i];
        sendArmPose();
    }   
}

void XGO::sendOrder(uint8_t addr,uint8_t data){
    OrderPacket packet;
    packet.addr = addr;
    packet.length = 1;
    packet.message[0] = data;
    sendOrder(packet);
}

void XGO::sendOrder(uint8_t addr,uint8_t data_len,uint8_t* data){
    OrderPacket packet;
    packet.addr = addr;
    packet.length = data_len;
    for(int i=0;i<data_len;i++){
        packet.message[i] = data[i];
    }
    sendOrder(packet);
}

void XGO::sendOrder(OrderPacket packet){
    uint8_t data[50];
    data[0]=0x55;data[1]=0x00;
    data[2]=packet.length+8;
    data[3]=0x01;
    data[4]=packet.addr;
    data[5+packet.length] = data[2] + data[3] +data[4];
    for(int i=0;i<packet.length;i++){
        data[5+i] = packet.message[i];
        data[5+packet.length] += data[5+i];
    }
    data[5+packet.length] = ~data[5+packet.length];
    data[6+packet.length] = 0x00;
    data[7+packet.length] = 0xAA;
    ser.write(data,8+packet.length);
    for(int i=0;i<8+packet.length;i++){
    	std::cout<< (int)data[i]<< " ";
    }
    std::cout<<std::endl;
    
}

void XGO::orderCallback(const std_msgs::UInt8MultiArray& msg){
    sendOrder(msg.data[0],msg.data[1],(uint8_t*)msg.data.data()+2);
}

void XGO::action(uint8_t action_id){
    sendOrder(0x3E,action_id);
}

void XGO::reset(){
    action(0xFF);
}

void XGO::sendBodyPose(){
    for(int i=0;i<6;i++){
        sendOrder(0x33+i,float2uint8(body_pose[i],body_limit[i][0],body_limit[i][1]));
    }
}

void XGO::sendLegPose(){
    OrderPacket packet;
    packet.addr = 0x40;
    packet.length = 12;
    for(int i=0;i<12;i++){
        packet.message[i] = float2uint8(leg_pose[i],body_limit[i%3][0],body_limit[i%3][1]);
    }
    sendOrder(packet);
}

void XGO::sendArmPose(){
    sendOrder(0x71,float2uint8(arm_pose[0],arm_limit[0][0],arm_limit[0][1]));
    sendOrder(0x73,float2uint8(arm_pose[1],arm_limit[1][0],arm_limit[1][1]));
    sendOrder(0x74,float2uint8(arm_pose[2],arm_limit[2][0],arm_limit[2][1]));
}

void XGO::sendMotorAngle(){
    OrderPacket packet;
    packet.addr = 0x50;
    packet.length = 15;
    for(int i=0;i<15;i++){
        if(i<12)
            packet.message[i] = float2uint8(joint_angle[i],joint_limit[i%3][0],joint_limit[i%3][1]);
        else
            packet.message[i] = float2uint8(joint_angle[i],joint_limit[i-9][0],joint_limit[i-9][1]);
    }
    sendOrder(packet);
}

void XGO::sendSpeed(){
    sendOrder(0x30,float2uint8(vx,-vx_max,vx_max));
    sendOrder(0x31,float2uint8(vy,-vy_max,vy_max));
    sendOrder(0x32,float2uint8(vyaw,-vyaw_max,vyaw_max));
}

void XGO::pubJointState(){
    if(!enable_joint_gui){
        sensor_msgs::JointState jointState;
        jointState.header.stamp = ros::Time::now();
        jointState.name={"13_Joint", "12_Joint", "11_Joint", "23_Joint", "22_Joint", "21_Joint", "33_Joint", "32_Joint", "31_Joint", "43_Joint", "42_Joint", "41_Joint", "53_Joint", "52_Joint", "51_Joint", "50_Joint", "500_Joint"};
        jointState.position={joint_angle[2],joint_angle[1],joint_angle[0],-joint_angle[5],joint_angle[4],joint_angle[3],-joint_angle[8],joint_angle[7],joint_angle[6],joint_angle[11],joint_angle[10],joint_angle[9],-joint_angle[14],joint_angle[13],joint_angle[12],joint_angle[12]/110.0,-joint_angle[12]/110.0};
        pub_joint_.publish(jointState);
    }
}


void XGO::pubBaseTf(){
    std_msgs::Float32MultiArray pos;
    pos.data.push_back(0.0);pos.data.push_back(0.0);pos.data.push_back(0.0);
    q.setRPY(imu_angle[0],imu_angle[1],imu_angle[2]);
    ts.setOrigin(tf::Vector3(0.0,0.0,0.12));
    ts.setRotation(q);
    br.sendTransform(tf::StampedTransform(ts,ros::Time::now(),"world","base_link"));
}
