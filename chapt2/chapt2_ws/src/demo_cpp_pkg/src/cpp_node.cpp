#include "rclcpp/rclcpp.hpp"

int main(int argc, char **argv)
{
  rclcpp::init(argc, argv); // 初始化工作，分配资源
  auto node = std::make_shared<rclcpp::Node>("cpp_node");
  RCLCPP_INFO(node->get_logger(), "你好 C++ 节点！");
  rclcpp::spin(node); // 进入循环，等待回调函数被触发
  rclcpp::shutdown(); // 释放资源
  return 0;
}