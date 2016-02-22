#!/usr/bin/python
import roslib
import sys
import rospy
import cv2
from std_msgs.msg import String
from sensor_msgs.msg import Image,CameraInfo
from cv_bridge import CvBridge, CvBridgeError
import numpy as np
from yaml import load, dump
import time

class image_converter:

  def __init__(self):
    self.bridge = CvBridge()
    self.image_sub = rospy.Subscriber("/camera/rgb/image_color",Image,self.imgCallback)
    # rospy.Timer(rospy.Duration(0.5), self.saveImg)

  def imgCallback(self,data):
    try:
      #Colour Image
      # self.cv_image = self.bridge.imgmsg_to_cv2(data, "bgr8")
          cv2.imwrite("/vol/hd/owncloud/PhD/Datasets/WhyConDataSet/accuracy/ar/" + str(time.ctime().replace(" ","_")) + ".png", self.bridge.imgmsg_to_cv2(data, "bgr8"))
    except CvBridgeError, e:
          print e

  def saveImg(self,_):
    cv2.imwrite("/vol/hd/owncloud/PhD/Datasets/WhyConDataSet/accuracy/new/" + str(time.ctime().replace(" ","_")) + ".png", self.cv_image)

def main(args):
  rospy.init_node('saveImage', anonymous=True)
  ic = image_converter()
  try:
    rospy.spin()
  except KeyboardInterrupt:
    print "Shutting down"
  # cv2.destroyAllWindows()

if __name__ == '__main__':
    main(sys.argv)