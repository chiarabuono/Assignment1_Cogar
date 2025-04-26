#!/usr/bin/env python3

import rospy
import random

from nav_msgs.msg import Odometry
from sensor_msgs.msg import Range, LaserScan

from assignments.msg import Map 

class Localization:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.z = 0

        self.trajectory_publisher = rospy.Publisher("trajectory", , queue_size=10)

        self.rbgd_sub = rospy.Subscriber("/xtion/rgb/image_raw", Image, self.rgbd_callback)
        self.odom_sub = rospy.Subscriber("/mobile_base_controller/odom", Odometry, self.odometry_callback)
        self.lidar_sub = rospy.Subscriber("/scan", LaserScan, self.lidar_callback)
        self.sonar_sub = rospy.Subscriber("/sonar_base", Range, self.sonar_callback)

        self.map_sub = rospy.Subscriber("map", Map, self.map_callback)
        
        rospy.loginfo(f"Damage detection node active")


    def rgbd_callback(self, msg): 
        self.x = self.x + 1
        
    def odometry_callback(self, msg): 
        self.x = self.x - 1

    def lidar_callback(self, msg): 
        self.y = self.y + 1

    def sonar_callback(self, msg): 
        self.y = self.y - 1
    
    def map_callback(self, msg):
        self.z = self.z - 1
 
    def run(self):
        rate = rospy.Rate(100) 
        while not rospy.is_shutdown():
            self.position_publisher.publish(Point(self.x, self.y, self.z))

            rate.sleep()

if __name__ == '__main__':
    node = DamageDetection()
    node.run()
