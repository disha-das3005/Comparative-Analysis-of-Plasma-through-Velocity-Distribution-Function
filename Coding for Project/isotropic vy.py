import numpy as np
import matplotlib.pyplot as plt
import math

r=np.linspace(0,1,num=100000)
print("random number btw o to 1=",r);
m=9.11*10**(-31);
print("mass of the elctron=",m);
T=3;
print("Temperature of plasma=",T);
Eps=(3/2)*T;
print("the value of epsilon=",Eps);
eg=1.602*10**(-19);
print("charge of electron=",eg);
z=np.sin(2*np.pi*r);
print("The value of sin phi=", z);
x=np.sin(np.arccos(1-r));
print("The value of sin theta=", x);
p=np.cos(np.arccos(1-r));
print("The value of cos theta=", p);
C=2/np.pi;
print("Normalisation Constant=",C);

vy=(((2*eg*Eps)/m)**0.5)*x*z;
print("The values of vx plasma=",vy);

vpf= C*((Eps)**0.5)*(np.exp((-m*vy*vy)/(2*eg*T)))
print("The values of vpf ",vpf)



fig , ax= plt.subplots()
ax.plot(vy,vpf,color="blue")
plt.xlabel('vy - axis')
plt.ylabel('vpf - axis')
plt.title(' Isotropic plasma Vy vs. VDF graph !')
plt.legend()
plt.show()
