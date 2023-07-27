import numpy as np
import matplotlib.pyplot as plt
import math

r=np.linspace(0,1,num=100000)
print("random number btw o to 1=",r);
m=9.11*10**(-31);
K=8.62*10**(-5)
T1=1292657.704
T2=1452
ka=20

V01=(((2*ka-3)*K*T1)/(ka*m))**0.5
V02=(((2*ka-3)*K*T2)/(ka*m))**0.5

z=np.cos(2*np.pi*r);
print("The value of cos phi=", z);
x=np.sin(np.arccos((1-r)**0.5));
print("The value of sin theta=", x);
p=np.cos(np.arccos((1-r)**0.5));
print("The value of cos theta=", p);

vx1=V01*x*z
vx2=V02*x*z

vpf1=1/((1+(x*x*z*z))**(ka+1))
vpf2=1/((1+(x*x*z*z))**(ka+1))

fig , ax= plt.subplots()
ax.plot(vx1,vpf1,color="red")
ax.plot(vx2,vpf2,color="orange")

plt.xlabel('V - axis')
plt.ylabel('Vdf - axis')
plt.title('kappa distribution of sun core !')
plt.legend()
plt.show()
