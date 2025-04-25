#!/usr/bin/env python3
from assignments.msg import Velocities
from assignments.srv import Destination, DestinationResponse

class TrajectoryControl:
    def __init__(self):
        self.walls = []
        self.victims = []

        service = rospy.Service('/movement_destination', Destination, self.destination_callback)

        self.velocities_publisher = rospy.Publisher("motor_velocities", Velocities, queue_size=10)

        self.map_sub = rospy.Subscriber("map", Map, self.map_callback)
        self.localization_sub = rospy.Subscriber("localization_sub", Point, self.localization_callback)

        rospy.loginfo(f"Trajectory control node active")

    def destination_callback(self, req):
        self.velocities_publisher.publish(Velocities(random.rand() * 10,
            random.rand() * 10 , random.rand() * 10, random.rand() * 10 ))
        return DestinationResponse(True)

    def map_callback(self, msg):
        pass

    def localization_callback(self, msg):
        pass

    def run(self):
        rate = rospy.Rate(100) 
        while not rospy.is_shutdown():
            # TODO: manage map completion
            self.map_publisher.publish(Map(self.walls, self.victims, False)) 

            rate.sleep()

if __name__ == '__main__':
    node = DamageDetection()
    node.run()

