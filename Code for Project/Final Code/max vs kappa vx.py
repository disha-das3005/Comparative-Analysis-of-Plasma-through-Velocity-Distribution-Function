import numpy as np
import matplotlib.pyplot as plt
import math

r=np.linspace(0,1,num=100000)
print("random number btw o to 1=",r);
m=9.11*10**(-31);
K=8.62*10**(-5)
T=3
Eps=(3/2)*T;
C=1;
eg=1.602*10**(-19);

ka1=30
V01=(((2*ka1-3)*K*T)/(ka1*m))**0.5

z=np.cos(2*np.pi*r);
print("The value of cos phi=", z);
x=np.sin(np.arccos((1-r)**0.5));
print("The value of sin theta=", x);
p=np.cos(np.arccos((1-r)**0.5));
print("The value of cos theta=", p);

vx1=V01*x*z
vx2=(((2*eg*Eps)/m)**0.5)*x*z;
vpf1=1/((1+(x*x*z*z))**(ka1+1))
vpf2= C*((Eps)**0.5)*(np.exp((-m*vx2*vx2)/(2*eg*T)))

fig , ax= plt.subplots()
ax.plot(vx1,vpf1,color="red")
ax.plot(vx2,vpf2,color="blue")
plt.xlabel('Vx - axis')
plt.ylabel('Vdf - axis')
plt.title('kappa distribution vs. maxwellian distribution !')
plt.legend()
plt.show()
