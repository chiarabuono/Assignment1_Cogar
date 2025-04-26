#!/usr/bin/env python3

# TODO: rename to risk_classificator
import rospy
import random

from assignments.msg import Cracks, Wall
from assignments.srv import Destination, DestinationRequest, DamageReport, DamageReportRequest
from geometry_msgs.msg import Point

severities = ["Negligible", "Marginal", "Serious", "Major", "Catastrophic"]

class DamageDetection:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.z = 0

        rospy.init_node('damage_detection')
        self.subscriber = rospy.Subscriber('cracks', Cracks, self.crack_analizer)
        self.subscriber = rospy.Subscriber('walls', Wall, self.wall_callback)

        self.trajectory_client = rospy.ServiceProxy('movement_destination', Destination)
        self.message_client = rospy.ServiceProxy('damage_message', DamageReport)

        rospy.loginfo(f"Damage detection node active")

    def crack_analizer(self, msg):
        num = random.randint(0, 10)

        if (msg.n_cracks == 0): 
            rospy.loginfo(f"No cracks")

        elif (num < 2): 
            rospy.loginfo(f"Not enough information, moving closer")
            destination = DestinationRequest(Point(random.random() * 100, random.random() * 100))
            self.trajectory_client(destination)

        else:
            rospy.loginfo(f"Wall classified")
            self.message_client(DamageReportRequest(Point(self.x, self.y, self.z), severities[random.randint(0, len(severities) -1)]))
    
    def wall_callback(self, msg):
        self.x = msg.position.x
        self.y = msg.position.y
        self.z = msg.position.z

    def run(self):
        rospy.spin()

if __name__ == '__main__':
    node = DamageDetection()
    node.run()
