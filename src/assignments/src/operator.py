#!/usr/bin/env python3
import rospy
import random

from std_msgs.msg import String, Bool, Int32
from sensor_msgs.msg import Image
from assignments.srv import Alert, AlertResponse


class Operator:
    def __init__(self):
        # TODO: how is it called this topic?
        self.subscriber_alert = rospy.Subscriber("NOOOOOOOOOOOOOOOOOOODEEEEE", String, self.receive_alert) 
        self.subscriber_triage = rospy.Subscriber("NOOOOOOOOOOOOOOOOOOODEEEEE", String, self.receive_triage) 

    def receive_alert(self, msg):
        rospy.loginfo("Alert received")

    def receive_triage(self, msg):
        rospy.loginfo("Received triage, sending human transport")
        

    
if __name__ == '__main__':
    rospy.init_node('operator_node')

    operator = Operator()
    
    rate = rospy.Rate(1) 
    while not rospy.is_shutdown():
     
        rate.sleep()
        
