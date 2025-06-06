#!/usr/bin/env python3

import rospy
import random

from std_msgs.msg import String
from assignments.msg import Cracks, Crack
from assignments.srv import DamageReport, DamageReportResponse, TriageReport, TriageReportResponse, VictimReport, VictimReportResponse

class MessageSender:
    def __init__(self):
        rospy.init_node('message_sender')

        # publisher used only for the integration testing purposes
        self.message_sender = rospy.Publisher('message_sender', String, queue_size=10) 

        rospy.Service('triage_message', TriageReport, self.triage_callback)
        rospy.Service('victim_detection_message', VictimReport, self.victim_callback)
        rospy.Service('damage_message', DamageReport, self.damage_callback)


    def victim_callback(self, req):
        self.message_sender.publish("victim")
        rospy.loginfo("Sending victim report")
        return VictimReportResponse(True)

    def damage_callback(self, req):
        self.message_sender.publish("damage")
        rospy.loginfo("Sending damage report")
        return DamageReportResponse(True)

    def triage_callback(self, req):
        self.message_sender.publish("triage")
        rospy.loginfo("Sending triage report")
        return TriageReportResponse(True)

    def run(self):
        rospy.spin()

if __name__ == '__main__':
    node = MessageSender()
    node.run()


