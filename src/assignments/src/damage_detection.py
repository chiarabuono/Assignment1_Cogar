#!/usr/bin/env python3

# TODO: rename to risk_classificator
import rospy
import random

from std_msgs.msg import String
from assignments.msg import Cracks, Crack
from assignments.srv import Destination, DestinationRequest

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
            destination = DestinationRequest(Point(rand.rand() * 100, rand.rand() * 100))
            self.trajectory_client(destination)

        else:
            class_classification = self.wall_classification(msg)
            self.publisher.publish(class_classification)
            rospy.loginfo(f"Wall classification: {class_classification}")
    
    def wall_callback(self, msg):
        



    def run(self):
        rospy.spin()

if __name__ == '__main__':
    node = DamageDetection()
    node.run()
