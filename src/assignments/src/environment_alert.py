#!/usr/bin/env python3
import rospy
import random

from std_msgs.msg import String
from assignments.msg import Cracks, Crack


class EnvironmentAlert:
    def __init__(self):
        rospy.init_node('environment_alert')
        self.subscriber = rospy.Subscriber("wall_classification", String, self.send_alarm)

        rospy.loginfo(f"Environment alert node active")
        

    def send_alarm(self, msg):
        num = random.randint(0, 10)

        if (msg.n_cracks == 0): 
            rospy.loginfo(f"No crack or week walls")

        else:
            class_classification = self.wall_classification(msg)
            self.publisher.publish(class_classification)
            rospy.loginfo(f"Wall classification: {class_classification}")
    



    def run(self):
        rospy.spin()

if __name__ == '__main__':
    node = EnvironmentAlert()
    node.run()
