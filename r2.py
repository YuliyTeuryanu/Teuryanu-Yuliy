import math
x=0.1722
y=6.33
z=3.25*(10**-4)
s=5*(math.atan(x))-(1/4)*(math.acos(x))*((x+3*(math.fabs(x-y))+x**2)/((math.fabs(x-y))*z+x**2))
g=round(s,3)
print(g)