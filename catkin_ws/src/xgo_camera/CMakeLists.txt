cmake_minimum_required(VERSION 3.0.2)
project(xgo_camera)

find_package(catkin REQUIRED COMPONENTS
  roscpp
  rospy
  std_msgs
  sensor_msgs
  message_generation
  message_runtime
)


## Generate messages in the 'msg' folder
# add_message_files(
#  FILES
#)

## Generate services in the 'srv' folder
# add_service_files(
#   FILES
#   Service1.srv
#   Service2.srv
# )

## Generate actions in the 'action' folder
# add_action_files(
#   FILES
#   Action1.action
#   Action2.action
# )

## Generate added messages and services with any dependencies listed here
#generate_messages(
#   DEPENDENCIES
#   std_msgs
#)

# generate_dynamic_reconfigure_options(
#   cfg/DynReconf1.cfg
#   cfg/DynReconf2.cfg
# )

catkin_package(
  INCLUDE_DIRS include
  LIBRARIES xgo_camera
  CATKIN_DEPENDS roscpp rospy std_msgs
#  DEPENDS system_lib
)

include_directories(
# include
  ${catkin_INCLUDE_DIRS}
)

#add_dependencies(
#${PROJECT_NAME}
#${${PROJECT_NAME}_EXPORTED_TARGETS}
#${catkin_EXPORTED_TARGETS}
#)

#target_link_libraries(${PROJECT_NAME}_node PUBLIC
#  ${catkin_LIBRARIES}
#)

catkin_install_python(PROGRAMS
   src/xgo_camera.py
   DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)

