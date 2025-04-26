#!/usr/bin/env python3

import rospy
import random

from std_msgs.msg import String
from assignments.srv import CloserInspection, CloserInspectionResponse, Destination, DestinationRequest

class CloserInspectionService:
    def __init__(self):
        rospy.init_node('closer_inspection')
        service = rospy.Service('closer_inspection', CloserInspection, self.closer_inspection_callback)
        self.destination_client = rospy.ServiceProxy('movement_destination', Destination)

    def closer_inspection_callback(self, req):
        self.destination_client(DestinationRequest(req.position))
        return CloserInspectionResponse(True)

    def run(self):
        rospy.spin()

if __name__ == '__main__':
    node = CloserInspectionService()
    node.run()


