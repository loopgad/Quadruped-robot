#ifndef __XGO_H
#define __XGO_H
#include <string>
#include <vector>
#include <ros/ros.h>
#include <string.h>
#include <geometry_msgs/Twist.h>
#include <serial/serial.h>
#include "std_msgs/Float32MultiArray.h"
#include "std_msgs/UInt8MultiArray.h"
#include "sensor_msgs/JointState.h"
#include <tf/tf.h>
#include <tf/transform_broadcaster.h>
#include <geometry_msgs/TransformStamped.h>
typedef struct{
    uint8_t addr;
    uint8_t length;
    uint8_t message[40];
}OrderPacket;

class XGO{
    public:
        XGO(ros::NodeHandle* nodehandle);
        void readState();
    private:
        ros::NodeHandle nh_;
        bool enable_joint_gui;
        XmlRpc::XmlRpcValue joint_limit_xml;
        XmlRpc::XmlRpcValue body_limit_xml;
        XmlRpc::XmlRpcValue arm_limit_xml;
        std::string com_port_str;
        char com_port[30];
        uint8_t rxFlag=0;
        uint8_t rxBuffer[256];
        uint8_t rxData[256];
        uint8_t rxPtr=0;

        ros::Subscriber sub_cmd_vel_;
        ros::Subscriber sub_body_pose_;
        ros::Subscriber sub_arm_pose_;
        ros::Subscriber sub_joint_angle_;
        ros::Subscriber sub_leg_pose_;
        ros::Subscriber sub_order_;
        serial::Serial ser;
        ros::Publisher pub_joint_;

        float vx=0;
        float vy=0;
        float vyaw=0;
        float battery;
        float body_pose[6]={0,0,108,0,0,0};
        float joint_angle[15];
        float leg_pose[12]={0,0,108,0,0,108,0,0,108,0,0,108};
        float arm_pose[3] = {85,85,3};
        float imu_angle[3];
        float imu_acc[3];
        float vx_max;
        float vy_max;
        float vyaw_max;

        tf::TransformBroadcaster br;
        tf::Transform ts;
        tf::Quaternion q;


        std::vector<float> period_limit;
        std::vector<std::vector<int>> joint_limit;
        std::vector<std::vector<int>> body_limit;
        std::vector<std::vector<int>> arm_limit;

        void sendSpeed();
        void sendOrder(uint8_t addr,uint8_t data);
        void sendOrder(uint8_t addr,uint8_t data_len,uint8_t* data);
        void action(uint8_t action_id);
        void reset();
        void sendMotorAngle();
        void updateState();
        void pubJointState();
        void pubBaseTf();
        void sendBodyPose();
        void sendLegPose();
        void sendArmPose();
        bool initParam();
        bool initCOM();
        void initSubcriber();
        void initPublisher();
        void sendOrder(OrderPacket packet);
        void cmdvelCallback(const geometry_msgs::Twist& msg);
        void legposeCallback(const std_msgs::Float32MultiArray& msg);
        void bodyposeCallback(const std_msgs::Float32MultiArray& msg);
        void jointangleCallback(const std_msgs::Float32MultiArray& msg);
        void armposeCallback(const std_msgs::Float32MultiArray& msg);
        void orderCallback(const std_msgs::UInt8MultiArray& msg);
};

float Saturation(float data,float min_limit,float max_limit);
uint8_t float2uint8(float data, float min_limit,float max_limit);
float uint82float(uint8_t data,float min_limit,float max_limit);

#endif
