#!/usr/bin/env python3
import rospy
import random

from std_msgs.msg import String, Bool, Int32
from sensor_msgs.msg import Image
from assignments.msg import Cracks, Crack
from assignments.srv import Alert, AlertResponse, WallStatus, WallStatusResponse

from sensor import *
from motor import Motor

class RobotController:
    def __init__(self):
        self.sensors = []
        self.motor = Motor()

    def add_sensor(self, sensor):
        self.sensors.append(sensor)

    def remove_sensor(self, sensor):
        self.sensors.remove(sensor)

    def detectVictim(self, msg):
        # print(msg.data)
        if msg.data == "not found": 
            rospy.loginfo("Person not found!")
            self.motor.move()

        elif msg.data == "not sure":
            rospy.loginfo("Not sure, approaching")
            self.motor.approach()
        else: 
            rospy.loginfo("Person found!")
            self.sendAlarm()
            self.evaluateCondition()
            

    def evaluateCondition(self):
        pass

    def detectStructure(self, msg):
        # TODO: FAI
        num = random.randint(0, 10)

        if (msg.n_cracks == 0): 
            rospy.loginfo(f"No cracks")
            self.motor.move()

        elif (num < 2): 
            rospy.loginfo(f"Not enough information")
            self.motor.approach()
        else:
            rospy.wait_for_service("/wall_classification")
            rospy.loginfo("Classification of the wall")
            classification_service = rospy.ServiceProxy("wall_classification", WallStatus)
            resp = classification_service(msg)
            
            rospy.loginfo(f"Wall classification: {resp}")

    def sendAlarm(self):
        rospy.wait_for_service('/person_alert')
        rospy.loginfo("Sending alarm")
        try:
            alert_service = rospy.ServiceProxy('/person_alert', Alert)
            resp = alert_service(True)
            rospy.loginfo(f"Person found successfully at position: {resp.positions}")
        except rospy.ServiceException as e:
            rospy.logerr(f"Service call failed: {e}")
        

    def notifySuccess(self):
        pass
        

    
if __name__ == '__main__':
    rospy.init_node('robot_node')

    robot = RobotController()
    robot.add_sensor(RgbSensor("rgb"))
    robot.add_sensor(MicSensor("mic"))
    
    rospy.Subscriber("victim_detected", String, robot.detectVictim)
    rospy.Subscriber('cracks', Cracks, robot.detectStructure)
    
    rate = rospy.Rate(1) 
    while not rospy.is_shutdown():
     
        rate.sleep()
        
