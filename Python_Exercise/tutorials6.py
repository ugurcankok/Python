import numpy as np
import cv2

drawing=False
mode=True
ix,iy=-1,-1


def draw_shape(event,x,y,flags,param):
    global ix,iy,drawing,mode

    if event==cv2.EVENT_LBUTTONDOWN:
        drawing=True
        ix,iy=x,y
    elif event==cv2.EVENT_MOUSEMOVE:
        if drawing==True:
            if mode==True:
                cv2.rectangle(img,(ix,iy),(x,y),(100,150,100),1)
            else:
                cv2.circle(img, (x, y), 10, (200,200,0),1)
    elif event==cv2.EVENT_LBUTTONUP:
        drawing=True
        if mode == True:
            cv2.rectangle(img, (ix, iy), (x, y), (100,150,100) ,1)
        else:
            cv2.circle(img,(x,y), 10, (200,200,0),1)

img=np.zeros((512,512,3),np.uint8)
cv2.namedWindow("image")
cv2.setMouseCallback("image",draw_shape)

while(1):
    cv2.imshow("image",img)
    k=cv2.waitKey(1) & 0xFF
    if k==ord("m"):
        mode=not mode
    elif k==27:
        break


cv2.destroyAllWindows()