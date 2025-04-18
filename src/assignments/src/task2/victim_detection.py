#!/usr/bin/env python3

import rospy
import random
from std_msgs.msg import Bool, Int32  # Add Int32 here
from sensor_msgs.msg import Image
from nav_msgs.msg import Odometry

# receive inform from RGB e Microphones
class VictimDetection:
    def __init__(self):
        rospy.init_node('victim_detection_node')
        
        self.rbg_sub = rospy.Subscriber("/xtion/rgb/image_raw", Image, self.image_processing)
        self.mic_sub = rospy.Subscriber("/mic", Int32, self.mic_callback)
        self.publisher = rospy.Publisher("/victim_detected", Bool, queue_size=1)

        self.person_in_image = False 
        self.heard_person = False

        rospy.loginfo("Victim detection node is ready!")

    def image_processing(self, msg): 
        num = random.randint(1, 1000)

        if num < 100:
            self.person_in_image = False
        else:
            self.person_in_image = True

    def mic_callback(self, msg):

        if msg.data < 100:  
            self.heard_person = False
        else:
            self.heard_person = True

    def odom_callback(self, msg):
        self.robot_position = msg


    def run(self):
        rate = rospy.Rate(1) 
        while not rospy.is_shutdown():
            if self.person_in_image and self.heard_person:
                rospy.loginfo("Person found!")
                self.publisher.publish(Bool(True))

            elif self.person_in_image or self.heard_person:
                rospy.loginfo("Not sure, approaching")
                self.publisher.publish(Bool(False))
            else:
                rospy.loginfo("No person")
                self.publisher.publish(Bool(False))
            
            rate.sleep()
        
if __name__ == '__main__':
    detect = VictimDetection()
    detect.run()
