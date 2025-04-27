#!/usr/bin/env python

import sys
import rospy
import unittest
from std_msgs.msg import String
from sensor_msgs.msg import Image

## A sample python unit test
class IntegrationTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        rospy.init_node('task1_integration_test', anonymous=True)
    
    def setUp(self):
        self.cracks_publishing = False

        self.subscriber = rospy.Subscriber('message_sender', String, self.message_sender_callback)

    def message_sender_callback(self, msg):
        if msg.data == 'damage':
            self.damage_message_sent = True

    def test_callback(self):
        rospy.sleep(2)  # Allow time for the subscriber to connect

        self.assertTrue(self.damage_message_sent)

if __name__ == '__main__':
    import rostest
    rostest.rosrun("assigments", 'task1_integration_test', IntegrationTest)
