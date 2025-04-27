#!/usr/bin/env python

import sys
import rospy
import unittest
from std_msgs.msg import String

## A sample python unit test
class IntegrationTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        rospy.init_node('task2_3_integration_test', anonymous=True)
    
    def setUp(self):
        self.victim_detected_message = False
        self.triage_message = False

        self.subscriber = rospy.Subscriber('message_sender', String, self.message_sender_callback)

    def message_sender_callback(self, msg):
        if msg.data == 'victim':
            self.victim_detected_message = True
        if msg.data == 'triage':
            self.triage_message = True

    def test_victim_detec(self):
        rospy.sleep(10)  # Allow time for the subscriber to connect

        self.assertTrue(self.victim_detected_message)

    def test_victim_triage(self):
        rospy.sleep(10)
        self.assertTrue(self.triage_message)

if __name__ == '__main__':
    import rostest
    rostest.rosrun("assigments", 'task2_3_integration_test', IntegrationTest)
