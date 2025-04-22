#!/usr/bin/env python3

import rospy
from audio_common_msgs.msg import AudioData
import numpy as np
import random

def generateAudio():
    rospy.init_node('microphoneNode')    
    pub = rospy.Publisher('/mic', AudioData, queue_size=10)

    while not rospy.is_shutdown():
        # Generate random audio signal (e.g., 3 seconds of random 16-bit PCM data)
        sample_rate = 44100  # 44.1 kHz
        duration = 3  # 3 seconds
        num_samples = sample_rate * duration
        random_signal = (np.random.rand(num_samples) * 65536 - 32768).astype(np.int16)

        # Convert the random signal to bytes and publish
        audio_msg = AudioData()
        audio_msg.data = random_signal.tobytes()
        pub.publish(audio_msg)

        # Sleep for a random duration between 1 and 20 seconds
        random_sleep_duration = random.uniform(1, 20)
        rospy.sleep(random_sleep_duration)

if __name__ == '__main__':
    try:
        generateAudio()
    except rospy.ROSInterruptException:
        pass
