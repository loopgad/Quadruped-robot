# generated from genmsg/cmake/pkg-genmsg.cmake.em

message(STATUS "xgo_ros: 4 messages, 0 services")

set(MSG_I_FLAGS "-Ixgo_ros:/home/pi/catkin_ws/src/xgo_ros/msg;-Istd_msgs:/opt/ros/noetic/share/std_msgs/cmake/../msg")

# Find all generators
find_package(gencpp REQUIRED)
find_package(geneus REQUIRED)
find_package(genlisp REQUIRED)
find_package(gennodejs REQUIRED)
find_package(genpy REQUIRED)

add_custom_target(xgo_ros_generate_messages ALL)

# verify that message/service dependencies have not changed since configure



get_filename_component(_filename "/home/pi/catkin_ws/src/xgo_ros/msg/ArmPose.msg" NAME_WE)
add_custom_target(_xgo_ros_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "xgo_ros" "/home/pi/catkin_ws/src/xgo_ros/msg/ArmPose.msg" ""
)

get_filename_component(_filename "/home/pi/catkin_ws/src/xgo_ros/msg/BodyPose.msg" NAME_WE)
add_custom_target(_xgo_ros_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "xgo_ros" "/home/pi/catkin_ws/src/xgo_ros/msg/BodyPose.msg" ""
)

get_filename_component(_filename "/home/pi/catkin_ws/src/xgo_ros/msg/LegPose.msg" NAME_WE)
add_custom_target(_xgo_ros_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "xgo_ros" "/home/pi/catkin_ws/src/xgo_ros/msg/LegPose.msg" ""
)

get_filename_component(_filename "/home/pi/catkin_ws/src/xgo_ros/msg/JointAngle.msg" NAME_WE)
add_custom_target(_xgo_ros_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "xgo_ros" "/home/pi/catkin_ws/src/xgo_ros/msg/JointAngle.msg" ""
)

#
#  langs = gencpp;geneus;genlisp;gennodejs;genpy
#

### Section generating for lang: gencpp
### Generating Messages
_generate_msg_cpp(xgo_ros
  "/home/pi/catkin_ws/src/xgo_ros/msg/ArmPose.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/xgo_ros
)
_generate_msg_cpp(xgo_ros
  "/home/pi/catkin_ws/src/xgo_ros/msg/BodyPose.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/xgo_ros
)
_generate_msg_cpp(xgo_ros
  "/home/pi/catkin_ws/src/xgo_ros/msg/LegPose.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/xgo_ros
)
_generate_msg_cpp(xgo_ros
  "/home/pi/catkin_ws/src/xgo_ros/msg/JointAngle.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/xgo_ros
)

### Generating Services

### Generating Module File
_generate_module_cpp(xgo_ros
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/xgo_ros
  "${ALL_GEN_OUTPUT_FILES_cpp}"
)

add_custom_target(xgo_ros_generate_messages_cpp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_cpp}
)
add_dependencies(xgo_ros_generate_messages xgo_ros_generate_messages_cpp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/pi/catkin_ws/src/xgo_ros/msg/ArmPose.msg" NAME_WE)
add_dependencies(xgo_ros_generate_messages_cpp _xgo_ros_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/pi/catkin_ws/src/xgo_ros/msg/BodyPose.msg" NAME_WE)
add_dependencies(xgo_ros_generate_messages_cpp _xgo_ros_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/pi/catkin_ws/src/xgo_ros/msg/LegPose.msg" NAME_WE)
add_dependencies(xgo_ros_generate_messages_cpp _xgo_ros_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/pi/catkin_ws/src/xgo_ros/msg/JointAngle.msg" NAME_WE)
add_dependencies(xgo_ros_generate_messages_cpp _xgo_ros_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(xgo_ros_gencpp)
add_dependencies(xgo_ros_gencpp xgo_ros_generate_messages_cpp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS xgo_ros_generate_messages_cpp)

### Section generating for lang: geneus
### Generating Messages
_generate_msg_eus(xgo_ros
  "/home/pi/catkin_ws/src/xgo_ros/msg/ArmPose.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/xgo_ros
)
_generate_msg_eus(xgo_ros
  "/home/pi/catkin_ws/src/xgo_ros/msg/BodyPose.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/xgo_ros
)
_generate_msg_eus(xgo_ros
  "/home/pi/catkin_ws/src/xgo_ros/msg/LegPose.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/xgo_ros
)
_generate_msg_eus(xgo_ros
  "/home/pi/catkin_ws/src/xgo_ros/msg/JointAngle.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/xgo_ros
)

### Generating Services

### Generating Module File
_generate_module_eus(xgo_ros
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/xgo_ros
  "${ALL_GEN_OUTPUT_FILES_eus}"
)

add_custom_target(xgo_ros_generate_messages_eus
  DEPENDS ${ALL_GEN_OUTPUT_FILES_eus}
)
add_dependencies(xgo_ros_generate_messages xgo_ros_generate_messages_eus)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/pi/catkin_ws/src/xgo_ros/msg/ArmPose.msg" NAME_WE)
add_dependencies(xgo_ros_generate_messages_eus _xgo_ros_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/pi/catkin_ws/src/xgo_ros/msg/BodyPose.msg" NAME_WE)
add_dependencies(xgo_ros_generate_messages_eus _xgo_ros_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/pi/catkin_ws/src/xgo_ros/msg/LegPose.msg" NAME_WE)
add_dependencies(xgo_ros_generate_messages_eus _xgo_ros_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/pi/catkin_ws/src/xgo_ros/msg/JointAngle.msg" NAME_WE)
add_dependencies(xgo_ros_generate_messages_eus _xgo_ros_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(xgo_ros_geneus)
add_dependencies(xgo_ros_geneus xgo_ros_generate_messages_eus)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS xgo_ros_generate_messages_eus)

### Section generating for lang: genlisp
### Generating Messages
_generate_msg_lisp(xgo_ros
  "/home/pi/catkin_ws/src/xgo_ros/msg/ArmPose.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/xgo_ros
)
_generate_msg_lisp(xgo_ros
  "/home/pi/catkin_ws/src/xgo_ros/msg/BodyPose.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/xgo_ros
)
_generate_msg_lisp(xgo_ros
  "/home/pi/catkin_ws/src/xgo_ros/msg/LegPose.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/xgo_ros
)
_generate_msg_lisp(xgo_ros
  "/home/pi/catkin_ws/src/xgo_ros/msg/JointAngle.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/xgo_ros
)

### Generating Services

### Generating Module File
_generate_module_lisp(xgo_ros
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/xgo_ros
  "${ALL_GEN_OUTPUT_FILES_lisp}"
)

add_custom_target(xgo_ros_generate_messages_lisp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_lisp}
)
add_dependencies(xgo_ros_generate_messages xgo_ros_generate_messages_lisp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/pi/catkin_ws/src/xgo_ros/msg/ArmPose.msg" NAME_WE)
add_dependencies(xgo_ros_generate_messages_lisp _xgo_ros_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/pi/catkin_ws/src/xgo_ros/msg/BodyPose.msg" NAME_WE)
add_dependencies(xgo_ros_generate_messages_lisp _xgo_ros_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/pi/catkin_ws/src/xgo_ros/msg/LegPose.msg" NAME_WE)
add_dependencies(xgo_ros_generate_messages_lisp _xgo_ros_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/pi/catkin_ws/src/xgo_ros/msg/JointAngle.msg" NAME_WE)
add_dependencies(xgo_ros_generate_messages_lisp _xgo_ros_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(xgo_ros_genlisp)
add_dependencies(xgo_ros_genlisp xgo_ros_generate_messages_lisp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS xgo_ros_generate_messages_lisp)

### Section generating for lang: gennodejs
### Generating Messages
_generate_msg_nodejs(xgo_ros
  "/home/pi/catkin_ws/src/xgo_ros/msg/ArmPose.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/xgo_ros
)
_generate_msg_nodejs(xgo_ros
  "/home/pi/catkin_ws/src/xgo_ros/msg/BodyPose.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/xgo_ros
)
_generate_msg_nodejs(xgo_ros
  "/home/pi/catkin_ws/src/xgo_ros/msg/LegPose.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/xgo_ros
)
_generate_msg_nodejs(xgo_ros
  "/home/pi/catkin_ws/src/xgo_ros/msg/JointAngle.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/xgo_ros
)

### Generating Services

### Generating Module File
_generate_module_nodejs(xgo_ros
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/xgo_ros
  "${ALL_GEN_OUTPUT_FILES_nodejs}"
)

add_custom_target(xgo_ros_generate_messages_nodejs
  DEPENDS ${ALL_GEN_OUTPUT_FILES_nodejs}
)
add_dependencies(xgo_ros_generate_messages xgo_ros_generate_messages_nodejs)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/pi/catkin_ws/src/xgo_ros/msg/ArmPose.msg" NAME_WE)
add_dependencies(xgo_ros_generate_messages_nodejs _xgo_ros_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/pi/catkin_ws/src/xgo_ros/msg/BodyPose.msg" NAME_WE)
add_dependencies(xgo_ros_generate_messages_nodejs _xgo_ros_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/pi/catkin_ws/src/xgo_ros/msg/LegPose.msg" NAME_WE)
add_dependencies(xgo_ros_generate_messages_nodejs _xgo_ros_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/pi/catkin_ws/src/xgo_ros/msg/JointAngle.msg" NAME_WE)
add_dependencies(xgo_ros_generate_messages_nodejs _xgo_ros_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(xgo_ros_gennodejs)
add_dependencies(xgo_ros_gennodejs xgo_ros_generate_messages_nodejs)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS xgo_ros_generate_messages_nodejs)

### Section generating for lang: genpy
### Generating Messages
_generate_msg_py(xgo_ros
  "/home/pi/catkin_ws/src/xgo_ros/msg/ArmPose.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/xgo_ros
)
_generate_msg_py(xgo_ros
  "/home/pi/catkin_ws/src/xgo_ros/msg/BodyPose.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/xgo_ros
)
_generate_msg_py(xgo_ros
  "/home/pi/catkin_ws/src/xgo_ros/msg/LegPose.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/xgo_ros
)
_generate_msg_py(xgo_ros
  "/home/pi/catkin_ws/src/xgo_ros/msg/JointAngle.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/xgo_ros
)

### Generating Services

### Generating Module File
_generate_module_py(xgo_ros
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/xgo_ros
  "${ALL_GEN_OUTPUT_FILES_py}"
)

add_custom_target(xgo_ros_generate_messages_py
  DEPENDS ${ALL_GEN_OUTPUT_FILES_py}
)
add_dependencies(xgo_ros_generate_messages xgo_ros_generate_messages_py)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/pi/catkin_ws/src/xgo_ros/msg/ArmPose.msg" NAME_WE)
add_dependencies(xgo_ros_generate_messages_py _xgo_ros_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/pi/catkin_ws/src/xgo_ros/msg/BodyPose.msg" NAME_WE)
add_dependencies(xgo_ros_generate_messages_py _xgo_ros_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/pi/catkin_ws/src/xgo_ros/msg/LegPose.msg" NAME_WE)
add_dependencies(xgo_ros_generate_messages_py _xgo_ros_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/pi/catkin_ws/src/xgo_ros/msg/JointAngle.msg" NAME_WE)
add_dependencies(xgo_ros_generate_messages_py _xgo_ros_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(xgo_ros_genpy)
add_dependencies(xgo_ros_genpy xgo_ros_generate_messages_py)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS xgo_ros_generate_messages_py)



if(gencpp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/xgo_ros)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/xgo_ros
    DESTINATION ${gencpp_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_cpp)
  add_dependencies(xgo_ros_generate_messages_cpp std_msgs_generate_messages_cpp)
endif()

if(geneus_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/xgo_ros)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/xgo_ros
    DESTINATION ${geneus_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_eus)
  add_dependencies(xgo_ros_generate_messages_eus std_msgs_generate_messages_eus)
endif()

if(genlisp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/xgo_ros)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/xgo_ros
    DESTINATION ${genlisp_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_lisp)
  add_dependencies(xgo_ros_generate_messages_lisp std_msgs_generate_messages_lisp)
endif()

if(gennodejs_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/xgo_ros)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/xgo_ros
    DESTINATION ${gennodejs_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_nodejs)
  add_dependencies(xgo_ros_generate_messages_nodejs std_msgs_generate_messages_nodejs)
endif()

if(genpy_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/xgo_ros)
  install(CODE "execute_process(COMMAND \"/usr/bin/python3\" -m compileall \"${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/xgo_ros\")")
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/xgo_ros
    DESTINATION ${genpy_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_py)
  add_dependencies(xgo_ros_generate_messages_py std_msgs_generate_messages_py)
endif()
