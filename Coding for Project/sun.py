import numpy as np
import matplotlib.pyplot as plt
import math

r=np.linspace(0,1,num=100000)
print("random number btw o to 1=",r);
m=9.11*10**(-31);
T1=1292657.704;
T2=3
Eps1=(3/2)*T1;
Eps2=(3/2)*T2;
eg=1.602*10**(-19);
C=1;
z=np.cos(2*np.pi*r);
print("The value of cos phi=", z);
x=np.sin(np.arccos((1-r)**0.5));
print("The value of sin theta=", x);
p=np.cos(np.arccos((1-r)**0.5));
print("The value of cos theta=", p);

vx1=(((2*eg*Eps1)/m)**0.5)*x*z;
vx2=(((2*eg*Eps2)/m)**0.5)*x*z;
vpf1= C*((Eps1)**0.5)*(np.exp((-m*vx1*vx1)/(2*eg*T1)))
vpf2= C*((Eps2)**0.5)*(np.exp((-m*vx2*vx2)/(2*eg*T2)))

fig , ax= plt.subplots()
ax.plot(vx1,vpf1,color="red")
ax.plot(vx2,vpf2,color="blue")
plt.xlabel('vx - axis')
plt.ylabel('vpf - axis')
plt.title(' core of the sun  plasma Vx vs. VDF graph !')
plt.legend()
plt.show()
