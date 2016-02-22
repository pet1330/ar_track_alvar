#!/usr/bin/python
import rospy
import cv2
from sensor_msgs.msg import Image,CameraInfo
from cv_bridge import CvBridge, CvBridgeError
from std_msgs.msg import String
import time
import os


class myTest:
    

    def __init__(self):
        self.bridge = CvBridge()
        self.pub = rospy.Publisher("/testInput",String,queue_size=100000)
        self.rate = rospy.Rate(1)

    def test(self):
        for root, dirs, files in os.walk("/vol/hd/owncloud/PhD/Datasets/tom_whyconDataSet/WhyconProcessed/accuracy/ar"):
            for name in files:
                if name.endswith(".png"):
                    self.rate.sleep()
                    self.pub.publish("%s/%s" % (root, name))
                if rospy.is_shutdown():
                    return
                    
rospy.init_node('myTest', anonymous=True)
t = myTest()
t.test()


# "/camera_rgb_optical_frame"