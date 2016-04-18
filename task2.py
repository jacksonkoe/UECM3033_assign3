import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

def ode_system(y,t,a,b):
    y0, y1 = y
    a = 1.0
    b = 0.2
    dy_dt = [a*(y0-y0*y1), b*(-y1+y0*y1)]
    return dy_dt
    
y_initial = [0.1, 1.0]

t = np.linspace(0,5,100)
sol = odeint(ode_system,y_initial,t,args=(a, b))

#Graph of y0 and y1 against t
plt.plot(t, sol[:, 0], 'r', label='y0(t)')
plt.plot(t, sol[:, 1], 'b', label='y1(t)')
plt.title('Graph of y0 and y1 against t with y0(0)=0.1')
plt.legend(loc='best')
plt.xlabel('t')
plt.ylabel('y')
plt.grid()
plt.savefig('Graph_y0_y1_vs_t_0.1.jpg')
plt.show()

#Graph of y1 against y0
plt.plot(sol[:, 0],sol[:,1], 'r')
plt.title('Graph of y1 against y0 with y0(0) = 0.1')
plt.xlabel('y0')
plt.ylabel('y1')
plt.grid()
plt.savefig('Graph_y1_vs_y0_0.1.jpg')
plt.show()

y_initial = [0.11, 1.0]
sol2 = odeint(ode_system,y_initial,t,args=(a, b))

#Graph of y0 and y1 against t
plt.plot(t, sol2[:, 0], 'r', label='y0(t)')
plt.plot(t, sol2[:, 1], 'b', label='y1(t)')
plt.title('Graph of y0 and y1 against t with y0(0)=0.11')
plt.legend(loc='best')
plt.xlabel('t')
plt.ylabel('y')
plt.grid()
plt.savefig('Graph_y0_y1_vs_t_0.11.jpg')
plt.show()

#Graph of y1 against y0
plt.plot(sol2[:, 0],sol2[:,1], 'r')
plt.title('Graph of y1 against y0 with y0(0) = 0.11')
plt.xlabel('y0')
plt.ylabel('y1')
plt.grid()
plt.savefig('Graph_y1_vs_y0_0.11.jpg')
plt.show()
