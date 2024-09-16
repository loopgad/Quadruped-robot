import cv2
import numpy as np 
import rospy
from cv_bridge import CvBridge, CvBridgeError
from sensor_msgs.msg import Image


node = rospy.init_node("xgo_camera")
cap = cv2.VideoCapture(0)
image_pub = rospy.Publisher("/xgo_camera/image",Image,queue_size=1)
bridge = CvBridge()

while not rospy.is_shutdown():
   ret, frame = cap.read()
   b, g, r = cv2.split(frame)
   frame = cv2.merge((r, g, b))
   image_pub.publish(bridge.cv2_to_imgmsg(frame,"bgr8"))


cap.release()
cv2.destroyAllWindows()
