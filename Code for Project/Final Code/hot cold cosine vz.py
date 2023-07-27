import numpy as np
import matplotlib.pyplot as plt
import math

r=np.linspace(0,1,num=10000)
print("random number btw o to 1=",r);
m=9.11*10**(-31);
C=1;
eg=1.602*10**(-19);

T1=0.51
T2=2.58
T3=3.0248
T4=0.0431
T5=0.3016
T6=0.0176

Eps1=(3/2)*T1;
Eps2=(3/2)*T2;
Eps3=(3/2)*T3;
Eps4=(3/2)*T4;
Eps5=(3/2)*T5;
Eps6=(3/2)*T6;

x=np.cos(np.arccos((1-r)**0.5));
print("The value of cos theta=", x);

vz1=(((2*eg*Eps1)/m)**0.5)*x
vz2=(((2*eg*Eps2)/m)**0.5)*x
vz3=(((2*eg*Eps3)/m)**0.5)*x
vz4=(((2*eg*Eps4)/m)**0.5)*x
vz5=(((2*eg*Eps5)/m)**0.5)*x
vz6=(((2*eg*Eps6)/m)**0.5)*x

vpf1=C*((Eps1)**0.5)*(np.exp((-m*vz1*vz1)/(2*eg*T1)))
vpf2=C*((Eps2)**0.5)*(np.exp((-m*vz2*vz2)/(2*eg*T2)))
vpf3=C*((Eps3)**0.5)*(np.exp((-m*vz3*vz3)/(2*eg*T3)))
vpf4=C*((Eps4)**0.5)*(np.exp((-m*vz4*vz4)/(2*eg*T4)))
vpf5=C*((Eps5)**0.5)*(np.exp((-m*vz5*vz5)/(2*eg*T5)))
vpf6=C*((Eps6)**0.5)*(np.exp((-m*vz6*vz6)/(2*eg*T6)))

fig , ax= plt.subplots()
ax.plot(vz1,vpf1,color="red",label="Sun's surface(hot)")
ax.plot(vz2,vpf2,color="orange",label="Lightening(hot)")
ax.plot(vz3,vpf3,color="green",label="Earth's Magnetosphere(hot)")
ax.plot(vz4,vpf4,color="blue",label="Earth's ionosphere(cold)")
ax.plot(vz5,vpf5,color="purple",label="Rocket's exhaust(hot)")
ax.plot(vz6,vpf6,color="cyan",label="comet's tail(cold)")


plt.xlabel('Vz - axis')
plt.ylabel('Vdf - axis')
plt.title('cosine Vz vs VDF graph for some hot and cold plasma !')
plt.legend()
plt.show()
