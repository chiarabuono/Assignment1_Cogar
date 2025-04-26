#!/usr/bin/env python3

# TODO: rename to risk_classificator
import rospy
import random

from assignments.msg import Cracks, Wall
from assignments.srv import Destination, DestinationRequest
from geometry_msgs.msg import Point

class DamageDetection:
    def __init__(self):
        rospy.init_node('damage_detection')
        self.subscriber = rospy.Subscriber('cracks', Cracks, self.crack_analizer)
        self.subscriber = rospy.Subscriber('wall_identification', Wall, self.wall_callback)

        self.trajectory_client = rospy.ServiceProxy('movement_destination', Destination)

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
            class_classification = self.wall_classification(msg)
            self.publisher.publish(class_classification)
            rospy.loginfo(f"Wall classification: {class_classification}")
    
    def wall_callback(self, msg):
        pass

    def run(self):
        rospy.spin()

if __name__ == '__main__':
    node = DamageDetection()
    node.run()
