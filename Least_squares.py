import math
print ("Enter number of points")
n=int(input())
sum_x=0
sum_y=0
sum_xx=0
sum_xy=0
xpoints=[]
ypoints=[]
for i in range (i,n+i):
	print ("For point ",i)
	x=input("Enter x : ")
	y=input("Enter y : ")
	xpoints.append(x)
	ypoints.append(y)
	sum_x=sum_x+x
	sum_y=sum_y+y
	xx=x*x
	sum_xx=sum_xx+xx
	xy=x*y
	sum_xy=sum_xy+xy
a=(sum_x*sum_xx*sum_y)/(n*sum_xx-sum_x*sum_x)
b=(sum_x*sum_y+n*sum_xy)/(n*sum_xx-sum_x*sum_x)
print ("Pairs of points are : ")
for i in range (0,len(xpoints)):
	print xpoints[i],ypoints[i]
print ("The required striaght line is y = ",b,"x +",a)
