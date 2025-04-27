#!/usr/bin/env python3

import rospy
from assignments.msg import Wall, Map
from geometry_msgs.msg import Point
from sensor_msgs.msg import Image, LaserScan, Range
from nav_msgs.msg import Odometry

class MapBuilder:
    def __init__(self):
        rospy.init_node('map_builder')
        self.walls = []
        self.victims = []

        self.map_publisher = rospy.Publisher("map", Map, queue_size=10)

        self.wall_sub = rospy.Subscriber("/xtion/rgb/image_raw", Image, self.rgbd_callback)
        self.odom_sub = rospy.Subscriber("/mobile_base_controller/odom", Odometry, self.odometry_callback)
        self.lidar_sub = rospy.Subscriber("/scan", LaserScan, self.lidar_callback)
        self.sonar_sub = rospy.Subscriber("/sonar_base", Range, self.sonar_callback)

        self.localization_sub = rospy.Subscriber("localization", Point, self.localization_callback)

        self.victim_sub = rospy.Subscriber("victim_detected", Point, self.victim_callback)
        self.wall_sub = rospy.Subscriber("wall", Wall, self.wall_callback)
        
        rospy.loginfo(f"Map builder node active")


    def rgbd_callback(self, msg): 
        pass

    def odometry_callback(self, msg): 
        pass

    def lidar_callback(self, msg): 
        pass

    def sonar_callback(self, msg): 
        pass

    def sonar_callback(self, msg):
        pass

    def localization_callback(self, msg):
        pass

    def victim_callback (self, msg):
        self.victims.append(Point(msg.x, msg.y, msg.z))
    
    def wall_callback(self, msg):
        self.walls.append(Wall(Point(msg.position.x, msg.position.y, msg.position.y), msg.height, msg.width))

    def run(self):
        rate = rospy.Rate(100) 
        while not rospy.is_shutdown():
            # TODO: manage map completion
            self.map_publisher.publish([], [], False) # TODO: put real data here

            rate.sleep()

if __name__ == '__main__':
    node = MapBuilder()
    node.run()
