#!/usr/bin/env python3
import rospy
import random

from std_msgs.msg import String
from assignments.msg import Cracks, Crack
from assignments.srv import WallStatus, WallStatusResponse


class DamageDetection:
    def __init__(self):
        rospy.init_node('damage_detection')
        self.service = rospy.Service('/wall_classification', WallStatus, self.wall_classification)
        self.publisher = rospy.Publisher()

        rospy.loginfo(f"Damage detection node active")
        
    
    def wall_classification(self, msg):
        severity_counts = {}
        for i in range(msg.cracks.n_cracks):
            severity = msg.cracks.cracks[i].severity.data
            severity_counts[severity] = severity_counts.get(severity, 0) + 1


        max_severity = max(severity_counts, key=severity_counts.get)
        severity_msg = String(data=max_severity)

        #TODO: compute the wall position
        x_wall = random.randint(0, 10)
        y_wall = random.randint(0, 10)
        wall = Crack(x_wall, y_wall, severity_msg)

        return WallStatusResponse(wall)


    def run(self):
        rospy.spin()

if __name__ == '__main__':
    node = DamageDetection()
    node.run()