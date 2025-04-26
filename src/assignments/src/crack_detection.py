#!/usr/bin/env python3
import rospy
import random

from std_msgs.msg import String
from sensor_msgs.msg import Image
from assignments.msg import Cracks, Crack
from sensor_msgs.msg import Image, LaserScan, Range
from geometry_msgs.msg import Point

severities = ["Negligible", "Marginal", "Serious", "Major", "Catastrophic"]

class CrackDetection:
    def __init__(self):
        rospy.init_node('crack_detection')

        self.x = 0
        self.y = 0
        self.z = 0

        self.localization_sub = rospy.Subscriber("localization", Point, self.localization_callback) # TODO: check that circular dependency doesn't cause any problems
        self.publisher = rospy.Publisher('cracks', Cracks, queue_size=10)
        self.subscriber = rospy.Subscriber('/xtion/rgb/image_raw', Image, self.detect_cracks)
        self.lidar_sub = rospy.Subscriber("/scan", LaserScan, self.lidar_callback)
        self.sonar_sub = rospy.Subscriber("/sonar_base", Range, self.sonar_callback)

        rospy.loginfo(f"Crack detection node active")

    def lidar_callback(self, msg): 
        pass

    def sonar_callback(self, msg): 
        pass

    def localization_callback(self, msg):
        self.x = msg.x
        self.y = msg.y
        self.z = msg.z
        pass

    def detect_cracks(self, image):
        #rospy.loginfo(f"Received image with height: {image.height}, and width: {image.width}")

        n_cracks = random.randint(0,10)

        cracks = Cracks()
        cracks.n_cracks = n_cracks
        cracks.cracks = []
        for i in range(n_cracks):
            crack = Crack()
            crack.x = self.x + random.random() * 100
            crack.y = self.y + random.random() * 100
            crack.z = self.z + random.random() * 100

            crack.severity = String(severities[random.randint(0, len(severities) -1)])
            cracks.cracks.append(crack)

        self.publisher.publish(cracks)

    def run(self):
        rospy.spin()

if __name__ == '__main__':
    node = CrackDetection()
    node.run()
