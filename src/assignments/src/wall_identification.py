#!/usr/bin/env python3

import rospy
import random
from geometry_msgs.msg import Point 
from assignments.msg import Wall
from sensor_msgs.msg import Image, LaserScan, Range

class WallIdentification:
    def __init__(self):
        rospy.init_node('wall_identifcation_node')

        self.wall_x = 0
        self.wall_y = 0
        self.wall_z = 0

        self.wall_publisher = rospy.Publisher("wall", Wall, queue_size=10)

        self.rbgd_sub = rospy.Subscriber("/xtion/rgb/image_raw", Image, self.rgbd_callback)
        self.lidar_sub = rospy.Subscriber("/scan", LaserScan, self.lidar_callback)
        self.sonar_sub = rospy.Subscriber("/sonar_base", Range, self.sonar_callback)

        self.localization_sub = rospy.Subscriber("localization_sub", Point, self.localization_callback) # TODO: check that circular dependency doesn't cause any problems

        rospy.loginfo(f"Damage detection node active")


    def rgbd_callback(self, msg): 
        pass

    def lidar_callback(self, msg): 
        pass

    def sonar_callback(self, msg): 
        pass
    
    def localization_callback(self, msg):
        self.wall_x = msg.x + random.random() * 10
        self.wall_y = msg.y + random.random() * 10
        self.wall_z = msg.z + random.random() * 10
        pass
 
    def run(self):
        rate = rospy.Rate(1) 
        while not rospy.is_shutdown():
            send = random.randint(1, 20) <= 2
            if send:
                self.wall_publisher.publish(Point(self.wall_x, self.wall_y, self.wall_z), random.random()*100, random.random()*100)

            rate.sleep()

if __name__ == '__main__':
    node = WallIdentification()
    node.run()