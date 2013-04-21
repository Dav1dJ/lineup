#!/usr/bin/env python

import cv
import numpy

image2 = cv.LoadImageM("pic3.jpg")
small = cv.CreateImage((640,312), 8, 3)

cv.Resize(image2,small,cv.CV_INTER_LINEAR)
size = cv.GetSize(small)
x=size[0]
y=size[1]
	
temp = cv.CreateImage(size, 8, 3)

sat = cv.CreateImage(size, 8, 1)
notsat = cv.CreateImage(size, 8, 1)
new = cv.CreateImage(size, 8, 1)

cv.Split(small, sat, None, None, None)
cv.Threshold(sat, notsat, 100, 255, cv.CV_THRESH_BINARY)
cv.Dilate(notsat, notsat, cv.CreateStructuringElementEx(3, 3, 1, 1, cv.CV_SHAPE_ELLIPSE) , 2)

storage = cv.CreateMemStorage(0)
contour = cv.FindContours(notsat, storage, cv.CV_RETR_EXTERNAL , cv.CV_CHAIN_APPROX_NONE)
while contour:
	
		if cv.ContourArea(contour)<10:
        		contour2=contour
			cv.DrawContours(new, contour2, cv.RGB(255,255,255), cv.RGB(255,255,255), -1, cv.CV_FILLED, cv.CV_AA)
		contour = contour.h_next()  

cv.SaveImage("stars.png", new)
cv.SaveImage("small.png", small)

for i in range(0,x):
	for j in range(0,y):	
		if new[j,i] ==255:
			p1y=j
			p1x=i 
			for k in range(0,x):
				for l in range(0,y):	
					if new[l,k] ==255:
						p2y=l
						p2x=k 
						dist=numpy.sqrt(numpy.power(p2x-p1x,2)+numpy.power(p2y-p1y,2))
						if dist<80 and dist>10:
							cv.Line(small, (p1x,p1y),(p2x,p2y), cv.RGB(255,255,0), 2, cv.CV_AA)

cv.SaveImage("small.png", small)
