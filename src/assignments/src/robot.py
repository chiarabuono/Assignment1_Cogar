#!/usr/bin/env python3
import rospy
import random

from std_msgs.msg import String, Bool, Int32
from sensor_msgs.msg import Image
from assignments.msg import Cracks, Crack
from assignments.srv import Alert, AlertResponse, WallStatus, WallStatusResponse

from sensor import *
from motor import MotorController

class RobotController:
    def __init__(self):
        #self.sensors = []
        self.motor = MotorController()

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
            # TODO: implement x and y to approach
            x = 0
            y = 0
            self.motor.approach(x, y)
        else: 
            rospy.loginfo("Person found!")
            self.sendAlarm("person")
            self.evaluateCondition()
            

    def evaluateCondition(self):
        pass

    def detectStructure(self, msg):
        if msg.severity.data == "None": 
            rospy.loginfo("No dangerous structures found!")
            self.motor.move()

        elif msg.severity.data == "not sure":
            rospy.loginfo("Not sure, approaching")
            self.motor.approach(msg.x, msg.y)
        else: 
            rospy.loginfo("Critical wall found")
            self.sendAlarm("person")
            # TODO: what else needs to be done?

    def sendAlarm(self, typeObject):
        rospy.loginfo("Sending alarm")
        if (typeObject == "person"):
            rospy.wait_for_service('/person_alert')
            alert_service = rospy.ServiceProxy('/person_alert', Alert)

        elif (typeObject == "wall"):
            rospy.wait_for_service('/environment_alert')
            alert_service = rospy.ServiceProxy('/environment_alert', Alert)
            #TODO implement wall alert
       
        try:
            resp = alert_service(True)
            rospy.loginfo(f"{typeObject} at position: {resp.positions}. Send alarm correctly.")
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
    rospy.Subscriber('wall_classification', Crack, robot.detectStructure)
    
    rate = rospy.Rate(1) 
    while not rospy.is_shutdown():
     
        rate.sleep()
        
