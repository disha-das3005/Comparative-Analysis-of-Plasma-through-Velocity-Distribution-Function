import numpy as np
import matplotlib.pyplot as plt
import math

r=np.linspace(0,1,num=100000)
print("random number btw o to 1=",r);
m=9.11*10**(-31);
K=8.62*10**(-5)
T=0.0389

ka1=3
ka2=30
ka3=20
ka4=2
ka5=15
ka6=9/2


V01=(((2*ka1-3)*K*T)/(ka1*m))**0.5
V02=(((2*ka2-3)*K*T)/(ka2*m))**0.5
V03=(((2*ka3-3)*K*T)/(ka3*m))**0.5
V04=(((2*ka4-3)*K*T)/(ka4*m))**0.5
V05=(((2*ka5-3)*K*T)/(ka5*m))**0.5
V06=(((2*ka6-3)*K*T)/(ka6*m))**0.5


z=np.sin(2*np.pi*r);
print("The value of sin phi=", z);
x=np.sin(np.arccos((1-r)**0.5));
print("The value of sin theta=", x);
p=np.cos(np.arccos((1-r)**0.5));
print("The value of cos theta=", p);

vy1=V01*x*z
vy2=V02*x*z
vy3=V03*x*z
vy4=V04*x*z
vy5=V05*x*z
vy6=V06*x*z


vpf1=1/((1+(x*x*z*z))**(ka1+1))
vpf2=1/((1+(x*x*z*z))**(ka2+1))
vpf3=1/((1+(x*x*z*z))**(ka3+1))
vpf4=1/((1+(x*x*z*z))**(ka4+1))
vpf5=1/((1+(x*x*z*z))**(ka5+1))
vpf6=1/((1+(x*x*z*z))**(ka6+1))


fig , ax= plt.subplots()
ax.plot(vy1,vpf1,color="red")
ax.plot(vy2,vpf2,color="orange")
ax.plot(vy3,vpf3,color="green")
ax.plot(vy4,vpf4,color="blue")
ax.plot(vy5,vpf5,color="purple")
ax.plot(vy6,vpf6,color="cyan")

plt.xlabel('Vy - axis')
plt.ylabel('Vdf - axis')
plt.title('kappa distribution of dusty plasma !')
plt.legend()
plt.show()
