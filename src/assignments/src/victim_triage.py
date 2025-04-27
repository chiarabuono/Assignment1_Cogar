#!/usr/bin/env python3

import rospy
import random
from std_msgs.msg import Bool, Int32, String
from geometry_msgs.msg import Point
from sensor_msgs.msg import Image
from audio_common_msgs.msg import AudioData
from assignments.srv import TriageReport, TriageReportRequest, Speaker, SpeakerRequest

class VictimTriage:
    def __init__(self):
        self.victim_position = Point()

        rospy.init_node('victimTriageNode')
        
        self.rgbdSub = rospy.Subscriber("/xtion/rgb/image_raw", Image, self.checkMovement)
        self.mic_sub = rospy.Subscriber("/mic", AudioData, self.audioAnalisysCallback)
        self.victimDetectedSub = rospy.Subscriber("victim_detected", Point, self.VictimDetectionCallback)

        rospy.wait_for_service('speaker')
        self.speaker_client = rospy.ServiceProxy('speaker', Speaker)
        rospy.wait_for_service('triage_message')
        self.message_client = rospy.ServiceProxy('triage_message', TriageReport)

        self.message_client(TriageReportRequest(self.victim_position, 99))

        self.personIsMoving = False 
        self.victimDetected = False
        self.response = False

        self.responseTime = rospy.Time.now()

        rospy.loginfo("Victim triage node is ready!")

    def VictimDetectionCallback(self, msg):
        self.victim_position = msg
        self.victimDetected = True

    def checkMovement(self, msg): 
        rand = random.randint(1, 100)

        if rand < 50:
            self.personIsMoving = False
        else:
            self.personIsMoving = True

    def audioAnalisysCallback(self, msg):
        rand = random.randint(1, 100)

        if rand < 50:  
            self.response = False
        else:
            self.response = True

    def run(self):
        rate = rospy.Rate(1)

        # even tho the waiting times in the documentation are reported as 10 
        # they have been reduced to speed up the test
        # this is acceptable since its a dummy component
        while not rospy.is_shutdown():
            if self.victimDetected:
                self.responseTime = rospy.Time.now()
                if self.personIsMoving:
                    self.responseTime = rospy.Time.now()
                    self.speaker_client(SpeakerRequest("Are you ok ?"))
                    rospy.loginfo("Asking victim if they are okay...")
                    
                    # Wait for up to 10 seconds for a response
                    response_received = False
                    start_time = rospy.Time.now()
                    
                    while (rospy.Time.now() - start_time).to_sec() < 2:
                        if self.response:
                            response_received = True
                            break
                        rospy.sleep(0.5)

                    if response_received:
                        elapsed = (rospy.Time.now() - self.responseTime).to_sec()
                        self.message_client(TriageReportRequest(self.victim_position, int(elapsed)))
                        rospy.loginfo(f"Victim responded in {int(elapsed)} seconds.")
                    else:
                        rospy.loginfo("No response from victim. Publishing code 99.")
                        self.message_client(TriageReportRequest(self.victim_position, 99))

                        self.response = False
                        self.victimDetected = False
                        self.personIsMoving = False
                    self.victimDetected = False
                else:
                    elapsed = (rospy.Time.now() - self.responseTime).to_sec()
                    if elapsed > 2:
                        rospy.loginfo("Person is dead")
                        self.message_client(TriageReportRequest(self.victim_position, 99))
                        self.response = False
                        self.victimDetected = False
                        self.personIsMoving = False
            else: 
                rospy.loginfo("Waiting for person")
            rate.sleep()

            
        
if __name__ == '__main__':
    node = VictimTriage()
    node.run()