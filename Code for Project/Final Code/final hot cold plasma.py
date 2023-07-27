import numpy as np
import matplotlib.pyplot as plt
import math
 
r=np.linspace(0,1,num=10000)
print("random number btw o to 1=",r);
m=9.11*10**(-31);
print("mass of the elctron=",m);
T1=30;
print("Temperature of hot plasma=",T1);
T2=4;
print("Temperature of cold plasma=",T2);

Eps1=(3/2)*T1;
print("the value of epsilon=",Eps1);
Eps2=(3/2)*T2;
print("the value of epsilon=",Eps2);

eg=1.602*10**(-19);
print("charge of electron=",eg);

z=np.cos(2*np.pi*r);
print("The value of cos phi=", z);
x=np.sin(np.arccos((1-r)**0.5));
print("The value of sin theta=", x);
p=np.cos(np.arccos((1-r)**0.5));
print("The value of cos theta=", p);


vx1=(((2*eg*Eps1)/m)**0.5)*x*z;
print("The values of vx of hot plasma=",vx1);
vx2=(((2*eg*Eps2)/m)**0.5)*x*z;
print("The values of vx of cold plasma=",vx2);
vx3=(((2*eg*Eps1)/m)**0.5)*x*z+(((2*eg*Eps2)/m)**0.5)*x*z;
print("The values of vx of hot plus cold plasma=",vx3);

vpf1= ((m/(2*eg))**0.5)*(np.exp((-m*vx1*vx1)/(2*eg*T1)))
print("The values of vpf of hot plasma",vpf1)
vpf2= ((m/(2*eg))**0.5)*(np.exp((-m*vx2*vx2)/(2*eg*T2)))
print("The values of vpf of cold plasma",vpf2)
vpf3= ((m/(2*eg))**0.5)*(np.exp((-m*vx1*vx1)/(2*eg*T1)))+((m/(2*eg))**0.5)*(np.exp((-m*vx2*vx2)/(2*eg*T2)))
print("The values of vpf of hot plus cold plasma",vpf3)

fig , ax= plt.subplots()
ax.plot(vx1,vpf1,color="red",label="hot")
ax.plot(vx2,vpf2,color="blue",label="cold")
ax.plot(vx2,vpf3,color="green",label="hot plus cold")
plt.xlabel('vx - axis')
plt.ylabel('vpf - axis')
plt.title(' Hot and Cold cosine plasma VX vs. VDF graph !')
plt.legend()
plt.show()
