import numpy as np
import matplotlib.pyplot as plt
import math
 
r=np.linspace(0,1,num=10000)
print("random number btw o to 1=",r);
m=9.11*10**(-31);
print("mass of the elctron=",m);
k=8.62*10**(-5);
print("Boltzman constant=",k);
T1=3;
print("Temperature of hot plasma=",T1);
T2=4;
print("Temperature of cold plasma=",T2);
Eps1=3*T1*r;
print("the value of epsilon=",Eps1);
Eps2=3*T2*r;
print("the value of epsilon=",Eps2);
eg=1.602*10**(-19);
print("charge of electron=",eg);
z=np.cos(2*np.pi*r);
print("The value of cos phi=", z);
x=np.sin(np.arccos((1-r)**0.5));
print("The value of sin theta=", x);
p=np.cos(np.arccos((1-r)**0.5));
print("The value of cos theta=", p);


vz1=(((2*eg*Eps1)/m)**0.5)*x*z;
print("The values of vz of hot plasma=",vz1);
vpf1= ((m/(2*eg))**0.5)*(np.exp((-m*vz1*vz1)/(2*eg*T1)))
print("The values of vpf of hot plasma",vpf1)
fig , ax= plt.subplots()
ax.plot(vz1,vpf1,color="red",label="hot")
plt.show()
