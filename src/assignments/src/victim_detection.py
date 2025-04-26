#!/usr/bin/env python3

import rospy
import random
from geometry_msgs.msg import Point 
from sensor_msgs.msg import Image
from audio_common_msgs.msg import AudioData # sudo apt install ros-${ROS_DISTRO}-audio-common-msgs

class VictimDetection:
    def __init__(self):
        rospy.init_node('victim_detection_node')
        
        self.rbg_sub = rospy.Subscriber("/xtion/rgb/image_raw", Image, self.image_processing)
        self.mic_sub = rospy.Subscriber("/mic", AudioData, self.mic_callback)
        self.publisher = rospy.Publisher("victim_detected", Point, queue_size=1)

        self.person_in_image = False 
        self.heard_person = False
 
        rospy.loginfo("Victim detection node is ready!")

    def image_processing(self, msg): 
        self.person_in_image = msg

    def mic_callback(self, msg):
        if int(msg.data[0]) < 100:  
            self.heard_person = False
        else:
            self.heard_person = Trued_person = msg

    def image_processing(self, msg): 
        num = random.randint(1, 1000)

        if num < 100:
            self.person_in_image = False
        else:
            self.person_in_image = True


    def run(self):
        rate = rospy.Rate(1) 
        while not rospy.is_shutdown():
            #TODO: get robot position and add some value to it to simulate person position
            if self.person_in_image or self.heard_person:
                self.publisher.publish(Point(random.random() * 1000, random.random() * 1000, random.random()*1000))

            rate.sleep()
        
if __name__ == '__main__':
    detect = VictimDetection()
    detect.run()