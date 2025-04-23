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

        rospy.loginfo(f"Damage detection node active")
        
    
    def wall_classification(self, msg):
        severity_counts = {}
        for i in range(msg.n_cracks):
            if (msg.cracks[i].severity.data not in severity_counts): 
                severity_counts[msg.cracks[i].severity.data] = 1
            else: 
                severity_counts[msg.cracks[i].severity.data] += 1

        max_severity = max(severity_counts, key=severity_counts.get)

        #TODO: compute the wall position
        x_wall = random.randint(0, 10)
        y_wall = random.randint(0, 10)
        wall = Crack(x_wall, y_wall, max_severity)

        return WallStatusResponse(wall)


    def run(self):
        rospy.spin()

if __name__ == '__main__':
    node = DamageDetection()
    node.run()