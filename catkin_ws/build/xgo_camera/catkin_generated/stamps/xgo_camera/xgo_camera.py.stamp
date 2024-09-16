import cv2
import numpy as np 
 
cap = cv2.VideoCapture(0) 
cv2.namedWindow("fig", cv2.WINDOW_NORMAL)
while(1):
   # get a frame
   ret, frame = cap.read()
   b, g, r = cv2.split(frame)
   frame = cv2.merge((r, g, b))
   # show a frame
   cv2.imshow("fig", frame)
   cv2.resizeWindow("fig",600,450)
   if cv2.waitKey(1) & 0xFF == ord('q'):
   #退出并拍照
       cv2.imwrite("takephoto2.jpg", frame)
       
       print("take Photo Ok")
       break
cap.release()
cv2.destroyAllWindows()
