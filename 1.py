import cv2
import numpy as np
import pyautogui as pg

low_blue = np.array([100, 100, 70])
high_blue = np.array([112, 255, 255])

'''low_green=np.array([50,80,50])
high_green=np.array([80,255,255])
low_yellow=np.array([30,70,50])
high_yello=np.array([35,255,255])'''

videofeed=cv2.VideoCapture(0)
#kernel=np.ones((3,3))
x1=0
y1=0
pg.moveTo(500,700)
pg.FAILSAFE=False
count=0
while True:
    _,frame=videofeed.read()
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    image_blue=cv2.inRange(hsv,low_blue,high_blue)
    '''blur=cv2.GaussianBlur(image_blue,(3,3),0)
    erode=cv2.erode(blur,kernel,iterations=3)
    dilute=cv2.dilate(erode,kernel,iterations=3)'''
    contour,_=cv2.findContours(image_blue,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE) 
    if contour!=[]:
        biggest=max(contour,key=cv2.contourArea)
        M=cv2.moments(biggest)
        if M['m00']>0:
            x=int(M['m10']/M['m00'])
            y=int(M['m01']/M['m00'])  
        #cv2.circle(frame,(x,y),7,(0,255,0),-1)
        if x1!=0:
            p1=4*(x-x1)
            p2=4*(y-y1)
            
            pg.move(-p1,p2,0.1)
            if p1<10 and p2<10:
                count+=1
            if count>20:
                count=0
                pg.click()
        x1=x
        y1=y
    '''#cv2.imshow('frame',frame)
    k=cv2.waitKey(1)
    if k==ord('e'):
        break'''
videofeed.release()