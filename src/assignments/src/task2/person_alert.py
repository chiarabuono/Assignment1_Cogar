#!/usr/bin/env python3

import rospy
import random
from std_msgs.msg import Bool, Int32  
from nav_msgs.msg import Odometry

# receive inform from RGB e Microphones
class PersonAlert:
    def __init__(self):
        rospy.init_node('person_alert_node')
        
        self.odom_sub = rospy.Subscriber("/mobile_base_controller/odom", Odometry, self.odom_callback)
        self.person_pos_pub = rospy.Publisher("/person_position", Odometry, queue_size=1)
        self.subscriber = rospy.Subscriber("/victim_detected", Bool, self.send_alarm)

        self.robot_position = Odometry()

        rospy.loginfo("Person alert node is ready!")


    def odom_callback(self, msg):
        self.robot_position = msg

    def compute_person_position(self):
        rospy.loginfo("Computing person position")
        person_position = self.robot_position
        person_position.pose.pose.position.x += random.randint(-100, 100)
        person_position.pose.pose.position.y += random.randint(-100, 100)
        
        return person_position

    def send_alarm(self, msg):
        if msg.data:
            self.person_pos_pub.publish(self.compute_person_position()) 
            rospy.loginfo(f"Sending alarm with person position")

    def run(self):
        rate = rospy.Rate(1) 
        rospy.spin()
        
if __name__ == '__main__':
    detect = PersonAlert()
    detect.run()
