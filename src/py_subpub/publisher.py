import rclpy
from rclpy.node import Node

from std_msgs.msg import UInt32

from datetime import datetime

class MinimalPublisher(Node):

    def __init__(self):
        super().__init__('minimal_publisher')
        self.publisher_ = self.create_publisher(UInt32, 'topic', 10)
        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0

    def timer_callback(self):
        now = datetime.now()
        msg = UInt32()
        msg.data = now.time().microsecond
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing %i at %i' % (self.i, msg.data))
        self.i += 1


def main(args=None):
    rclpy.init(args=args)

    minimal_publisher = MinimalPublisher()

    rclpy.spin(minimal_publisher)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()