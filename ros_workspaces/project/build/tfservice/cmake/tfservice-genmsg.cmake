# generated from genmsg/cmake/pkg-genmsg.cmake.em

message(STATUS "tfservice: 0 messages, 5 services")

set(MSG_I_FLAGS "-Istd_msgs:/opt/ros/indigo/share/std_msgs/cmake/../msg;-Igeometry_msgs:/opt/ros/indigo/share/geometry_msgs/cmake/../msg;-Isensor_msgs:/opt/ros/indigo/share/sensor_msgs/cmake/../msg;-Itf2_msgs:/opt/ros/indigo/share/tf2_msgs/cmake/../msg;-Iactionlib_msgs:/opt/ros/indigo/share/actionlib_msgs/cmake/../msg")

# Find all generators
find_package(gencpp REQUIRED)
find_package(genlisp REQUIRED)
find_package(genpy REQUIRED)

add_custom_target(tfservice_generate_messages ALL)

# verify that message/service dependencies have not changed since configure



get_filename_component(_filename "/home/cc/ee106a/fa15/class/ee106a-ai/ros_workspaces/project/src/tfservice/srv/tfSrv.srv" NAME_WE)
add_custom_target(_tfservice_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "tfservice" "/home/cc/ee106a/fa15/class/ee106a-ai/ros_workspaces/project/src/tfservice/srv/tfSrv.srv" "geometry_msgs/Quaternion"
)

get_filename_component(_filename "/home/cc/ee106a/fa15/class/ee106a-ai/ros_workspaces/project/src/tfservice/srv/ImuSrv.srv" NAME_WE)
add_custom_target(_tfservice_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "tfservice" "/home/cc/ee106a/fa15/class/ee106a-ai/ros_workspaces/project/src/tfservice/srv/ImuSrv.srv" "geometry_msgs/Vector3"
)

get_filename_component(_filename "/home/cc/ee106a/fa15/class/ee106a-ai/ros_workspaces/project/src/tfservice/srv/exploreSrv.srv" NAME_WE)
add_custom_target(_tfservice_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "tfservice" "/home/cc/ee106a/fa15/class/ee106a-ai/ros_workspaces/project/src/tfservice/srv/exploreSrv.srv" ""
)

get_filename_component(_filename "/home/cc/ee106a/fa15/class/ee106a-ai/ros_workspaces/project/src/tfservice/srv/globalSrv.srv" NAME_WE)
add_custom_target(_tfservice_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "tfservice" "/home/cc/ee106a/fa15/class/ee106a-ai/ros_workspaces/project/src/tfservice/srv/globalSrv.srv" ""
)

get_filename_component(_filename "/home/cc/ee106a/fa15/class/ee106a-ai/ros_workspaces/project/src/tfservice/srv/NuSrv.srv" NAME_WE)
add_custom_target(_tfservice_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "tfservice" "/home/cc/ee106a/fa15/class/ee106a-ai/ros_workspaces/project/src/tfservice/srv/NuSrv.srv" "geometry_msgs/Transform:geometry_msgs/Quaternion:geometry_msgs/Vector3"
)

#
#  langs = gencpp;genlisp;genpy
#

### Section generating for lang: gencpp
### Generating Messages

### Generating Services
_generate_srv_cpp(tfservice
  "/home/cc/ee106a/fa15/class/ee106a-ai/ros_workspaces/project/src/tfservice/srv/exploreSrv.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/tfservice
)
_generate_srv_cpp(tfservice
  "/home/cc/ee106a/fa15/class/ee106a-ai/ros_workspaces/project/src/tfservice/srv/ImuSrv.srv"
  "${MSG_I_FLAGS}"
  "/opt/ros/indigo/share/geometry_msgs/cmake/../msg/Vector3.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/tfservice
)
_generate_srv_cpp(tfservice
  "/home/cc/ee106a/fa15/class/ee106a-ai/ros_workspaces/project/src/tfservice/srv/tfSrv.srv"
  "${MSG_I_FLAGS}"
  "/opt/ros/indigo/share/geometry_msgs/cmake/../msg/Quaternion.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/tfservice
)
_generate_srv_cpp(tfservice
  "/home/cc/ee106a/fa15/class/ee106a-ai/ros_workspaces/project/src/tfservice/srv/globalSrv.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/tfservice
)
_generate_srv_cpp(tfservice
  "/home/cc/ee106a/fa15/class/ee106a-ai/ros_workspaces/project/src/tfservice/srv/NuSrv.srv"
  "${MSG_I_FLAGS}"
  "/opt/ros/indigo/share/geometry_msgs/cmake/../msg/Transform.msg;/opt/ros/indigo/share/geometry_msgs/cmake/../msg/Quaternion.msg;/opt/ros/indigo/share/geometry_msgs/cmake/../msg/Vector3.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/tfservice
)

### Generating Module File
_generate_module_cpp(tfservice
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/tfservice
  "${ALL_GEN_OUTPUT_FILES_cpp}"
)

add_custom_target(tfservice_generate_messages_cpp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_cpp}
)
add_dependencies(tfservice_generate_messages tfservice_generate_messages_cpp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/cc/ee106a/fa15/class/ee106a-ai/ros_workspaces/project/src/tfservice/srv/tfSrv.srv" NAME_WE)
add_dependencies(tfservice_generate_messages_cpp _tfservice_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/cc/ee106a/fa15/class/ee106a-ai/ros_workspaces/project/src/tfservice/srv/ImuSrv.srv" NAME_WE)
add_dependencies(tfservice_generate_messages_cpp _tfservice_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/cc/ee106a/fa15/class/ee106a-ai/ros_workspaces/project/src/tfservice/srv/exploreSrv.srv" NAME_WE)
add_dependencies(tfservice_generate_messages_cpp _tfservice_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/cc/ee106a/fa15/class/ee106a-ai/ros_workspaces/project/src/tfservice/srv/globalSrv.srv" NAME_WE)
add_dependencies(tfservice_generate_messages_cpp _tfservice_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/cc/ee106a/fa15/class/ee106a-ai/ros_workspaces/project/src/tfservice/srv/NuSrv.srv" NAME_WE)
add_dependencies(tfservice_generate_messages_cpp _tfservice_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(tfservice_gencpp)
add_dependencies(tfservice_gencpp tfservice_generate_messages_cpp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS tfservice_generate_messages_cpp)

### Section generating for lang: genlisp
### Generating Messages

### Generating Services
_generate_srv_lisp(tfservice
  "/home/cc/ee106a/fa15/class/ee106a-ai/ros_workspaces/project/src/tfservice/srv/exploreSrv.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/tfservice
)
_generate_srv_lisp(tfservice
  "/home/cc/ee106a/fa15/class/ee106a-ai/ros_workspaces/project/src/tfservice/srv/ImuSrv.srv"
  "${MSG_I_FLAGS}"
  "/opt/ros/indigo/share/geometry_msgs/cmake/../msg/Vector3.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/tfservice
)
_generate_srv_lisp(tfservice
  "/home/cc/ee106a/fa15/class/ee106a-ai/ros_workspaces/project/src/tfservice/srv/tfSrv.srv"
  "${MSG_I_FLAGS}"
  "/opt/ros/indigo/share/geometry_msgs/cmake/../msg/Quaternion.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/tfservice
)
_generate_srv_lisp(tfservice
  "/home/cc/ee106a/fa15/class/ee106a-ai/ros_workspaces/project/src/tfservice/srv/globalSrv.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/tfservice
)
_generate_srv_lisp(tfservice
  "/home/cc/ee106a/fa15/class/ee106a-ai/ros_workspaces/project/src/tfservice/srv/NuSrv.srv"
  "${MSG_I_FLAGS}"
  "/opt/ros/indigo/share/geometry_msgs/cmake/../msg/Transform.msg;/opt/ros/indigo/share/geometry_msgs/cmake/../msg/Quaternion.msg;/opt/ros/indigo/share/geometry_msgs/cmake/../msg/Vector3.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/tfservice
)

### Generating Module File
_generate_module_lisp(tfservice
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/tfservice
  "${ALL_GEN_OUTPUT_FILES_lisp}"
)

add_custom_target(tfservice_generate_messages_lisp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_lisp}
)
add_dependencies(tfservice_generate_messages tfservice_generate_messages_lisp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/cc/ee106a/fa15/class/ee106a-ai/ros_workspaces/project/src/tfservice/srv/tfSrv.srv" NAME_WE)
add_dependencies(tfservice_generate_messages_lisp _tfservice_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/cc/ee106a/fa15/class/ee106a-ai/ros_workspaces/project/src/tfservice/srv/ImuSrv.srv" NAME_WE)
add_dependencies(tfservice_generate_messages_lisp _tfservice_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/cc/ee106a/fa15/class/ee106a-ai/ros_workspaces/project/src/tfservice/srv/exploreSrv.srv" NAME_WE)
add_dependencies(tfservice_generate_messages_lisp _tfservice_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/cc/ee106a/fa15/class/ee106a-ai/ros_workspaces/project/src/tfservice/srv/globalSrv.srv" NAME_WE)
add_dependencies(tfservice_generate_messages_lisp _tfservice_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/cc/ee106a/fa15/class/ee106a-ai/ros_workspaces/project/src/tfservice/srv/NuSrv.srv" NAME_WE)
add_dependencies(tfservice_generate_messages_lisp _tfservice_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(tfservice_genlisp)
add_dependencies(tfservice_genlisp tfservice_generate_messages_lisp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS tfservice_generate_messages_lisp)

### Section generating for lang: genpy
### Generating Messages

### Generating Services
_generate_srv_py(tfservice
  "/home/cc/ee106a/fa15/class/ee106a-ai/ros_workspaces/project/src/tfservice/srv/exploreSrv.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/tfservice
)
_generate_srv_py(tfservice
  "/home/cc/ee106a/fa15/class/ee106a-ai/ros_workspaces/project/src/tfservice/srv/ImuSrv.srv"
  "${MSG_I_FLAGS}"
  "/opt/ros/indigo/share/geometry_msgs/cmake/../msg/Vector3.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/tfservice
)
_generate_srv_py(tfservice
  "/home/cc/ee106a/fa15/class/ee106a-ai/ros_workspaces/project/src/tfservice/srv/tfSrv.srv"
  "${MSG_I_FLAGS}"
  "/opt/ros/indigo/share/geometry_msgs/cmake/../msg/Quaternion.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/tfservice
)
_generate_srv_py(tfservice
  "/home/cc/ee106a/fa15/class/ee106a-ai/ros_workspaces/project/src/tfservice/srv/globalSrv.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/tfservice
)
_generate_srv_py(tfservice
  "/home/cc/ee106a/fa15/class/ee106a-ai/ros_workspaces/project/src/tfservice/srv/NuSrv.srv"
  "${MSG_I_FLAGS}"
  "/opt/ros/indigo/share/geometry_msgs/cmake/../msg/Transform.msg;/opt/ros/indigo/share/geometry_msgs/cmake/../msg/Quaternion.msg;/opt/ros/indigo/share/geometry_msgs/cmake/../msg/Vector3.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/tfservice
)

### Generating Module File
_generate_module_py(tfservice
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/tfservice
  "${ALL_GEN_OUTPUT_FILES_py}"
)

add_custom_target(tfservice_generate_messages_py
  DEPENDS ${ALL_GEN_OUTPUT_FILES_py}
)
add_dependencies(tfservice_generate_messages tfservice_generate_messages_py)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/cc/ee106a/fa15/class/ee106a-ai/ros_workspaces/project/src/tfservice/srv/tfSrv.srv" NAME_WE)
add_dependencies(tfservice_generate_messages_py _tfservice_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/cc/ee106a/fa15/class/ee106a-ai/ros_workspaces/project/src/tfservice/srv/ImuSrv.srv" NAME_WE)
add_dependencies(tfservice_generate_messages_py _tfservice_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/cc/ee106a/fa15/class/ee106a-ai/ros_workspaces/project/src/tfservice/srv/exploreSrv.srv" NAME_WE)
add_dependencies(tfservice_generate_messages_py _tfservice_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/cc/ee106a/fa15/class/ee106a-ai/ros_workspaces/project/src/tfservice/srv/globalSrv.srv" NAME_WE)
add_dependencies(tfservice_generate_messages_py _tfservice_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/cc/ee106a/fa15/class/ee106a-ai/ros_workspaces/project/src/tfservice/srv/NuSrv.srv" NAME_WE)
add_dependencies(tfservice_generate_messages_py _tfservice_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(tfservice_genpy)
add_dependencies(tfservice_genpy tfservice_generate_messages_py)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS tfservice_generate_messages_py)



if(gencpp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/tfservice)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/tfservice
    DESTINATION ${gencpp_INSTALL_DIR}
  )
endif()
add_dependencies(tfservice_generate_messages_cpp std_msgs_generate_messages_cpp)
add_dependencies(tfservice_generate_messages_cpp geometry_msgs_generate_messages_cpp)
add_dependencies(tfservice_generate_messages_cpp sensor_msgs_generate_messages_cpp)
add_dependencies(tfservice_generate_messages_cpp tf2_msgs_generate_messages_cpp)

if(genlisp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/tfservice)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/tfservice
    DESTINATION ${genlisp_INSTALL_DIR}
  )
endif()
add_dependencies(tfservice_generate_messages_lisp std_msgs_generate_messages_lisp)
add_dependencies(tfservice_generate_messages_lisp geometry_msgs_generate_messages_lisp)
add_dependencies(tfservice_generate_messages_lisp sensor_msgs_generate_messages_lisp)
add_dependencies(tfservice_generate_messages_lisp tf2_msgs_generate_messages_lisp)

if(genpy_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/tfservice)
  install(CODE "execute_process(COMMAND \"/usr/bin/python\" -m compileall \"${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/tfservice\")")
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/tfservice
    DESTINATION ${genpy_INSTALL_DIR}
  )
endif()
add_dependencies(tfservice_generate_messages_py std_msgs_generate_messages_py)
add_dependencies(tfservice_generate_messages_py geometry_msgs_generate_messages_py)
add_dependencies(tfservice_generate_messages_py sensor_msgs_generate_messages_py)
add_dependencies(tfservice_generate_messages_py tf2_msgs_generate_messages_py)
