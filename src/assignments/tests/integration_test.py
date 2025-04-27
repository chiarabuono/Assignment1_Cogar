#!/usr/bin/env python

import sys
import rospy
import unittest
from sensor_msgs.msg import Image
from assignments.msg import Cracks, Wall

## A sample python unit test
class IntegrationTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        rospy.init_node('integration_test', anonymous=True)
    
    def setUp(self):
        self.cracks_publishing = False

        self.subscriber = rospy.Subscriber('cracks', Cracks, self.crack_callback)

    def crack_callback(self, msg):
        rospy.loginfo("received cracks")
        self.cracks_publishing = True

    def test_callback(self):
        rospy.sleep(0.2)  # Allow time for the subscriber to connect

        self.assertTrue(self.cracks_publishing)

if __name__ == '__main__':
    import rostest
    rostest.rosrun("assigments", 'integration_test', IntegrationTest)
