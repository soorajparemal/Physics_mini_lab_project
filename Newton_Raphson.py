def f(x):
	return (x*x)-n
def f1(x):
	return (2*x)
x=0.0
root=2.0
print ("Succesive approximation of the square root : ",n)
while abs(root-x)>0.0000001:
	x=root
	root=root-f(x)/f1(x)
	print (root)
