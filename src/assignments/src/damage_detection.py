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
        #self.service = rospy.Service('/wall_classification', WallStatus, self.wall_classification)
        self.publisher = rospy.Publisher("wall_classification", Crack, queue_size=1)

        rospy.loginfo(f"Damage detection node active")

    def crack_analizer(self, msg):
        num = random.randint(0, 10)

        if (msg.n_cracks == 0): 
            rospy.loginfo(f"No cracks")
            severity = "None"

        elif (num < 2): 
            rospy.loginfo(f"Not enough information")
            severity = "not sure"
            x_wall, y_wall = self.wall_position()
        else:
            x_wall, y_wall, severity = self.wall_classification(msg)
        wall = Crack(x_wall, y_wall, severity)
        self.publisher.publish(wall)

    def wall_position(self):
        # TODO: implement such that the robot knows where the wall is
        x_wall = random.randint(0, 10)
        y_wall = random.randint(0, 10)

        return x_wall, y_wall

        
    
    def wall_classification(self, msg):
        severity_counts = {}
        for i in range(msg.cracks.n_cracks):
            severity = msg.cracks.cracks[i].severity.data
            severity_counts[severity] = severity_counts.get(severity, 0) + 1


        max_severity = max(severity_counts, key=severity_counts.get)
        severity_msg = String(data=max_severity)

        x_wall, y_wall = self.wall_position()

        return x_wall, y_wall, severity_msg


    def run(self):
        rospy.spin()

if __name__ == '__main__':
    node = DamageDetection()
    node.run()