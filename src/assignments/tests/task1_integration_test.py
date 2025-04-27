#!/usr/bin/env python

import sys
import rospy
import unittest
from assignments.msg import Map
from std_msgs.msg import String
from sensor_msgs.msg import Image

## A sample python unit test
class IntegrationTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        rospy.init_node('task1_integration_test', anonymous=True)
    
    def setUp(self):
        self.cracks_publishing = False
        self.map_sent = False

        self.message_subscriber = rospy.Subscriber('message_sender', String, self.message_sender_callback)
        self.map_subscriber = rospy.Subscriber('map', Map, self.map_callback)

    def message_sender_callback(self, msg):
        if msg.data == 'damage':
            self.damage_message_sent = True

    def map_callback(self, msg):
        self.map_sent = True

    def test_damage_report(self):
        rospy.sleep(2)  # Allow time for the subscriber to connect

        self.assertTrue(self.damage_message_sent, "no test damage received")

    def test_map_creatione(self):
        rospy.sleep(2)  # Allow time for the subscriber to connect
        self.assertTrue(self.map_sent, "no map message received")
        

if __name__ == '__main__':
    import rostest
    rostest.rosrun("assigments", 'task1_integration_test', IntegrationTest)
