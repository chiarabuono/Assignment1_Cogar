#!/usr/bin/env python3
import rospy
import random

from std_msgs.msg import String
from assignments.msg import Cracks, Crack
from assignments.srv import WallStatus, WallStatusResponse


class DamageDetection:
    def __init__(self):
        rospy.init_node('damage_detection')
        self.subscriber = rospy.Subscriber('cracks', Cracks, self.crack_analizer)
        self.publisher = rospy.Publisher("wall_classification", String, queue_size=10)

        rospy.loginfo(f"Damage detection node active")
        

    def crack_analizer(self, msg):
        num = random.randint(0, 10)

        if (msg.n_cracks == 0): 
            rospy.loginfo(f"No cracks")

        elif (num < 2): 
            rospy.loginfo(f"Not enough information")
        else:
            class_classification = self.wall_classification(msg)
            self.publisher.publish(class_classification)
            rospy.loginfo(f"Wall classification: {class_classification}")
    
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
        wall = Crack(x_wall, y_wall, max_severity) # FIXME: this makes no sense

        return WallStatusResponse(wall)


    def run(self):
        rospy.spin()

if __name__ == '__main__':
    node = DamageDetection()
    node.run()
