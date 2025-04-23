#!/usr/bin/env python3
import rospy
import random
from abc import ABC, abstractmethod

from std_msgs.msg import String, Bool, Int32
from audio_common_msgs.msg import AudioData # sudo apt install ros-${ROS_DISTRO}-audio-common-msgs
from sensor_msgs.msg import Image
from assignments.msg import Cracks, Crack

class Sensor(ABC):
    def __init__(self, sensor_type):
        self.sensor_type = sensor_type
        self.receive_data()

    @abstractmethod
    def receive_data(self):
        # TODO: implement in the subclasses based on the sensor type
        # implement subscriber
        pass
    
    @abstractmethod
    def elaborate_data(self):
        # implement method that is called by the subscriber
        pass

class RgbSensor(Sensor):
    def receive_data(self):
        self.subscriber = rospy.Subscriber('/xtion/rgb/image_raw', Image, self.elaborate_data)
        
        # publisher
        self.publisher_crack = rospy.Publisher('cracks', Cracks, queue_size=10)
        self.publisher_person = rospy.Publisher("person_in_image", Bool, queue_size=10)
        self.severities = ["Negligible", "Marginal", "Serious", "Major", "Catastrophic"]
    
    def elaborate_data(self, data):
        self.crack_detection(data)
        self.person_detection(data)

    def crack_detection(self, image):
        n_cracks = random.randint(0,10)

        cracks = Cracks()
        cracks.n_cracks = n_cracks
        cracks.cracks = []
        for i in range(n_cracks):
            crack = Crack()
            crack.x = int(random.randint(1, image.width))
            crack.y = int(random.randint(1, image.height))
            crack.severity = String(self.severities[random.randint(0, len(self.severities) -1)])
            cracks.cracks.append(crack)

        self.publisher_crack.publish(cracks)

    def person_detection(self, msg):
        num = random.randint(1, 1000)

        if num < 100: self.publisher_person.publish(False)
        else: self.publisher_person.publish(True)
        

class MicSensor(Sensor):
    def receive_data(self):
        self.subscriber = rospy.Subscriber("/mic", AudioData, self.elaborate_data)
        self.publisher = rospy.Publisher("/victim_heard", Bool, queue_size=1)

    def elaborate_data(self, msg):
        num = random.randint(1, 1000)
        if num < 400:  self.publisher.publish(False)
        else: self.publisher.publish(True)