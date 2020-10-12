Screen Recorder using Open CV.

import numpy as np
import cv2
# for Mac & Windows users
from PIL import ImageGrab
# for linux users
# import pyscreenshot as ImageGrab

fourcc = cv2.VideoWriter_fourcc('X','V','I','D') #you can use other codecs as well.
out = cv2.VideoWriter('output.avi', fourcc, 8, (500,490))
while(True):
  # Capture Screen
  img = ImageGrab.grab()
  # Convert to numPy Array
  img_np = np.array(img)
  #frame = cv2.cvtColor(img_np, cv2.COLOR_BGR2GRAY)
  # Write frame to video writer
  out.write(img_np)
  # Show image on OpenCV frame
  cv2.imshow("frame", img_np)
  key = cv2.waitKey(1)
  if key == 27:
    break

vid.release()
cv2.destroyAllWindows()
