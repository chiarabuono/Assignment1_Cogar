#!/usr/bin/env python3
import rospy
import random

from std_msgs.msg import String
from assignments.msg import Cracks, Crack
from nav_msgs.msg import Odometry

trascurable_severities = ["Negligible", "Marginal"]

class EnvironmentAlert:
    def __init__(self):
        rospy.init_node('environment_alert')
        #self.subscriber = rospy.Subscriber("wall_classification", String, self.send_alarm)
        self.odom_sub = rospy.Subscriber("/mobile_base_controller/odom", Odometry, self.odom_callback)
        #self.publisher = rospy.Publisher("/environment_alarm", Crack, queue_size= 1)
        self.service = rospy.Publisher("/environment_alarm", Crack, queue_size= 1)

        self.robot_position = Odometry()

        rospy.loginfo(f"Environment alert node active")

    def odom_callback(self, msg):
        self.robot_position = msg

    def compute_danger_position(self):
        rospy.loginfo("Computing danger position")
        
        danger = Crack()
        danger.x = self.robot_position.pose.pose.position.x + random.randint(-100, 100)
        danger.y = self.robot_position.pose.pose.position.y + random.randint(-100, 100)
        danger.severity = self.severity

        return danger

    def send_alarm(self, msg):
        if msg.data and (msg.data not in trascurable_severities):
            self.severity = msg.data
            self.publisher.publish(self.compute_danger_position()) 
            rospy.loginfo(f"Sending alarm with wall position")   

    

    def run(self):
        rospy.spin()

if __name__ == '__main__':
    node = EnvironmentAlert()
    node.run()
