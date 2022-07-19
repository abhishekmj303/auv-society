#! /usr/bin/env python3

import rospy
from std_msgs.msg import String

def send_message():
    # Initialize the node and name it.
    pub = rospy.Publisher("msg_str", String, queue_size=1)
    rospy.init_node("sender")
    rate = rospy.Rate(10)

    # This is the publisher loop.
    while not rospy.is_shutdown():
        # Get the current node name and the message to publish.
        node_name = "["+rospy.get_name()+"]: "
        msg_str = input()

        # Publish the message.
        pub.publish(node_name+msg_str)
        rate.sleep()

if __name__ == "__main__":
    try:
        send_message()
    except rospy.ROSInterruptException:
        pass