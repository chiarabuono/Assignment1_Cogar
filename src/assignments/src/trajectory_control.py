#!/usr/bin/env python3
import rospy
import random

from assignments.msg import Map, Velocities
from assignments.srv import Destination, DestinationResponse

from geometry_msgs.msg import Point

class TrajectoryControl:
    def __init__(self):
        rospy.init_node('trajectory_control')
        self.walls = []
        self.victims = []

        service = rospy.Service('movement_destination', Destination, self.destination_callback)

        self.velocities_publisher = rospy.Publisher("motor_velocities", Velocities, queue_size=10)

        self.map_sub = rospy.Subscriber("map", Map, self.map_callback)
        self.localization_sub = rospy.Subscriber("localization", Point, self.localization_callback)

        rospy.loginfo(f"Trajectory control node active")

    def destination_callback(self, req):
        self.velocities_publisher.publish([random.random() * 10, random.random() * 10 , random.random() * 10, random.random() * 10 ])
        return DestinationResponse(True)

    def map_callback(self, msg):
        pass

    def localization_callback(self, msg):
        pass
        # TODO implment this callback

    def run(self):
        rospy.spin()

if __name__ == '__main__':
    node = TrajectoryControl()
    node.run()

