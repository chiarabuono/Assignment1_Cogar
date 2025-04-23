#!/usr/bin/env python3

import rospy
import random
from std_msgs.msg import Bool, Int32  
from nav_msgs.msg import Odometry
from assignments.srv import Alert, AlertResponse

class PersonAlert:
    def __init__(self):
        rospy.init_node('person_alert_node')
        
        self.odom_sub = rospy.Subscriber("/mobile_base_controller/odom", Odometry, self.odom_callback)
        # self.person_pos_pub = rospy.Publisher("/person_position", Odometry, queue_size=1)
        # self.subscriber = rospy.Subscriber("/victim_detected", Bool, self.send_alarm)
        self.service = rospy.Service('/person_alert', Alert, self.alert_callback)

        self.robot_position = Odometry()

        rospy.loginfo("Person alert node is ready!")


    def odom_callback(self, msg):
        self.robot_position = msg

    def alert_callback(self, req):
        rospy.loginfo(f"Received a message: {req.message}")
        if req.message:
            rospy.loginfo("Sending alarm with person position")
            # TODO: ask if we have to implement the operator
            person_position = self.compute_person_position()
            return AlertResponse(positions=person_position)


    def compute_person_position(self):
        rospy.loginfo("Computing person position")
        x = self.robot_position.pose.pose.position.x + random.uniform(-0.5, 0.5)
        y = self.robot_position.pose.pose.position.y + random.uniform(-0.5, 0.5)
        return [x, y]


    def run(self):
        rate = rospy.Rate(1) 
        rospy.spin()
        
if __name__ == '__main__':
    detect = PersonAlert()
    detect.run()
