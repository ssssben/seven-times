import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class Listener(Node):
    def __init__(self):
        super().__init__("listener")
        self.sub = self.create_subscription(String, "countup", self.cb, 10)
    def cb(self, msg):
        try:
            received_value = int(msg.data)
            multiplied = received_value * 7
            self.get_logger().info(f"7倍した結果: {multiplied} (7x{received_value})")
        except ValueError:
            self.get_logger().error(f"無効なデータを受信: {msg.data}")

def main():
    rclpy.init()
    node = Listener()
    rclpy.spin(node)
