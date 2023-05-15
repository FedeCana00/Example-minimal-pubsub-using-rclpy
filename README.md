# Example-minimal-pubsub-using-rclpy
## Introduction
Examples of minimal publisher/subscriber using rclpy.
<br><br>
In this example a talker sends the time in microseconds to the listener. This will compute the time difference between sending and receiving the message.
## Deployment
[ros2](https://docs.ros.org/en/foxy/Installation.html) must be installed in order to run the program.
<br>
Inside the folder run
```
source /opt/ros/foxy/setup.bash
colcon build
source/install/local_setup.bash
```
Finally run the **listener** node
```
ros2 run py_subpub listener
```
Do the same in another shell for the **talker** node.

