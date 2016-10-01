def f(x):
	return 1/(1+(x**2))
a=0
b=6
k=9
h=1.0
y=[]
integral=0.0
while k<=6:
	y.append(f(x))
	k+=h
integral=integral+y[0]+y[len(y)-1]
k=3
while k<= len(y)-2:
	integral=integral+(y[k]*4)+(y[k-1]*2)
	k+=2
integral=(integral*h)/3
print("within the limit " ,a,"and",b,"integral of given function")
print (integral)
