cmake_minimum_required(VERSION 3.5)
project(lidar_camera_calib)

# Default to C99
if(NOT CMAKE_C_STANDARD)
  set(CMAKE_C_STANDARD 99)
endif()

# Default to C++14
if(NOT CMAKE_CXX_STANDARD)
  set(CMAKE_CXX_STANDARD 14)
endif()

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  #add_compile_options(-Wall -Wextra -Wpedantic)
  #add_compile_options(-Wextra -Wpedantic)
endif()

find_package(ament_cmake REQUIRED)
find_package(cv_bridge REQUIRED)
find_package(pcl_conversions REQUIRED)
find_package(pcl_ros REQUIRED)
find_package(rclcpp REQUIRED)
find_package(rclpy REQUIRED)
find_package(sensor_msgs REQUIRED)
find_package(std_msgs REQUIRED)
find_package(PCL REQUIRED)
find_package(OpenCV)
find_package(Threads)
find_package(Ceres REQUIRED)
find_package(backward_ros REQUIRED)

set(CMAKE_AUTOMOC ON)
set(CMAKE_AUTOUIC ON)
set(CMAKE_AUTORCC ON)
set(CMAKE_INCLUDE_CURRENT_DIR ON)
include_directories(
  include
  ${ament_INCLUDE_DIRS}
  ${PCL_INCLUDE_DIRS}
  ${OpenCV_INCLUDE_DIRS}
)
link_directories(
  ${PCL_LIBRARY_DIRS}
)

add_executable(lidar_camera_calib src/lidar_camera_calib.cpp include/lidar_camera_calib.hpp)

target_link_libraries(lidar_camera_calib 
  ${ament_LIBRARIES} ${OpenCV_LIBS} ${PCL_LIBRARIES} ${CERES_LIBRARIES}
)

ament_target_dependencies(lidar_camera_calib
cv_bridge
pcl_conversions
pcl_ros
rclcpp
rclpy
sensor_msgs
std_msgs
backward_ros
  )

install(
  DIRECTORY "include/"
  DESTINATION include
)

install(
  DIRECTORY launch config
  DESTINATION share/${PROJECT_NAME}
)

install(TARGETS
lidar_camera_calib
  ARCHIVE DESTINATION lib
  LIBRARY DESTINATION lib
  RUNTIME DESTINATION bin
)

install(TARGETS 
lidar_camera_calib
  DESTINATION lib/${PROJECT_NAME}
)

ament_package()