#! /usr/bin/env python3

import sys
import rospy
from std_msgs.msg import String

def del_prev_line():
    # Escape sequence to delete the previous line.
    CURSOR_UP_BEGIN = '\x1B[F'
    ERASE_LINE = '\x1B[2K'
    sys.stdout.write(CURSOR_UP_BEGIN)
    sys.stdout.write(ERASE_LINE)
    sys.stdout.flush()

def callback(data):
    # Get the current and sender's names.
    current_name = rospy.get_name()[-1]
    sender_name = data.data.split("]")[0][-1]

    # If the sender is same as current, then
    if current_name == sender_name:
        # delete the previous line (taken for the input).
        del_prev_line()
    
    # Print the message.
    print(data.data)

def receiver():
    # Initialize the node and name it.
    rospy.init_node("receiver")
    rospy.Subscriber("msg_str", String, callback)
    rospy.spin()

if __name__ == "__main__":
    receiver()