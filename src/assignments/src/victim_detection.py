#!/usr/bin/env python3

import rospy
import random
from std_msgs.msg import String, Bool, Int32
from sensor_msgs.msg import Image
from nav_msgs.msg import Odometry

class VictimDetection:
    def __init__(self):
        rospy.init_node('victim_detection_node')
        
        self.rbg_sub = rospy.Subscriber("person_in_image", Bool, self.image_processing)
        self.mic_sub = rospy.Subscriber("/victim_heard", Bool, self.mic_callback)
        self.publisher = rospy.Publisher("/victim_detected", String, queue_size=1)

        self.person_in_image = False 
        self.heard_person = False

        rospy.loginfo("Victim detection node is ready!")

    def image_processing(self, msg): 
        self.person_in_image = msg

    def mic_callback(self, msg):
        self.heard_person = msg

    def run(self):
        rate = rospy.Rate(1) 
        while not rospy.is_shutdown():
            if self.person_in_image and self.heard_person:
                # rospy.loginfo("Person found!")
                self.publisher.publish("found")

            elif self.person_in_image or self.heard_person:
                # rospy.loginfo("Not sure, approaching")
                self.publisher.publish("not sure")

            else:
                # rospy.loginfo("No person")
                self.publisher.publish("not found")
            
            rate.sleep()
        
if __name__ == '__main__':
    detect = VictimDetection()
    detect.run()