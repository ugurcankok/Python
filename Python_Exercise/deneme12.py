import cv2
import numpy as np
import matplotlib as plt


img=cv2.imread("//Users//ugurcan//Desktop//image//Flag_of_Turkey.png")
#reflect = cv2.copyMakeBorder(img,15,15,15,15,cv2.BORDER_REFLECT)

#cv2.imshow("image",img)
#cv2.imshow("image1",reflect)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

height, width = img.shape[:2]
rotation_matrix = cv2.getRotationMatrix2D((width/2, height/2), 135, .5)
rotated_image = cv2.warpAffine(img, rotation_matrix, (width, height))
cv2.imshow("Rotated Image", rotated_image)
cv2.waitKey(0)
cv2.destroyAllWindows()