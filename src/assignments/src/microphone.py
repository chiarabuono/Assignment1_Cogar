#!/usr/bin/env python3

import rospy
import random
from std_msgs.msg import Int32

def microphone():
    rospy.init_node('microphone')
    pub = rospy.Publisher('/mic', Int32, queue_size=1)

    rate = rospy.Rate(0.5)

    while not rospy.is_shutdown():
        num = random.randint(1, 1000)
        #rospy.loginfo(f"Publishing random mic number: {num}")
        pub.publish(Int32(num))
        rate.sleep()

if __name__ == '__main__':
    microphone()
