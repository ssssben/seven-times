import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class Talker(Node):
    def __init__(self):
        super().__init__("talker")
        self.pub = self.create_publisher(String, "countup", 10)
        self.create_timer(1.0, self.timer_callback)
        self.count = 0

    def timer_callback(self):
        msg = String()
        msg.data = f"{self.count}"
        self.pub.publish(msg)
        self.get_logger().info(f"整数: '{msg.data}'")
        self.count += 1

def main():
    rclpy.init()
    node = Talker()
    rclpy.spin(node)
