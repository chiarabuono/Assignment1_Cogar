import rospy
import random

class Localization:
    def __init__(self):
        self.walls = []
        self.victims = []

        self.map_publisher = rospy.Publisher("map", Point, queue_size=10)

        self.wall_sub = rospy.Subscriber("/xtion/rgb/image_raw", Image, self.rgbd_callback)
        self.odom_sub = rospy.Subscriber("/mobile_base_controller/odom", Odometry, self.odometry_callback)
        self.lidar_sub = rospy.Subscriber("/scan", LaserScan, self.lidar_callback)
        self.sonar_sub = rospy.Subscriber("/sonar_base", Range, self.sonar_callback)

        self.localization_sub = rospy.Subscriber("localization_sub", Point, self.localization_callback) # TODO: check that circular dependency doesn't cause any problems

        self.victim_sub = rospy.Subscriber("victim_detected", Point, self.victim_callback)
        # self.wall_sub = rospy.Subscriber("victim_detected", Point, self.wall_callback) FIXME: wall identification missing
        
        rospy.loginfo(f"Map builder node active")


    # TODO: fix callbacks
    def rgbd_callback(self, msg): 
        pass

    def odometry_callback(self, msg): 
        pass

    def lidar_callback(self, msg): 
        pass

    def sonar_callback(self, msg): 
        pass

    def sonar_callback(self, msg):
        pass

    def victim_callback (self, msg):
        self.victims.append(msg)
    
    def wall_callback(self, msg):
        self.walls.append(msg)

    def run(self):
        rate = rospy.Rate(100) 
        while not rospy.is_shutdown():
            # TODO: manage map completion
            self.map_publisher.publish(Map(self.walls, self.victims, False)) 

            rate.sleep()

if __name__ == '__main__':
    node = DamageDetection()
    node.run()
