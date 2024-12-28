import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class Answer(Node):
    def __init__(self):
        super().__init__("answer")
        self.sub = self.create_subscription(String, "chatter", self.cb, 10)
    def cb(self, msg):
        try:
            received_value = int(msg.data)
            multiplied = received_value * 7
            self.get_logger().info(f"7倍した結果: {multiplied} (7x{received_value})")
        except ValueError:
            self.get_logger().error(f"無効なデータを受信: {msg.data}")

def main():
    rclpy.init()
    node = Answer()
    rclpy.spin(node)
