#!/usr/bin/env python3
import rospy
import random

from std_msgs.msg import String
from sensor_msgs.msg import Image
from assignments.msg import Cracks, Crack

severities = ["Negligible", "Marginal", "Serious", "Major", "Catastrophic"]

class CrackDetection:
    def __init__(self):
        rospy.init_node('crack_detection')
        self.publisher = rospy.Publisher('cracks', Cracks, queue_size=10)
        self.subscriber = rospy.Subscriber('/xtion/rgb/image_raw', Image, self.rgb_callback)

        rospy.loginfo(f"Crack detection node active")

    def rgb_callback(self, image):
        #rospy.loginfo(f"Received image with height: {image.height}, and width: {image.width}")

        n_cracks = random.randint(0,10)

        cracks = Cracks()
        cracks.n_cracks = n_cracks
        cracks.cracks = []
        for i in range(n_cracks):
            crack = Crack()
            # TODO: this are map coordinates, there should be some constant which bounds the size
            # it would aso make sense to have a z axis
            crack.x = random.rand() * 10000
            crack.y = random.rand() * 10000
            crack.severity = String(severities[random.randint(0, len(severities) -1)])
            cracks.cracks.append(crack)

        self.publisher.publish(cracks)

    def run(self):
        rospy.spin()

if __name__ == '__main__':
    node = CrackDetection()
    node.run()
