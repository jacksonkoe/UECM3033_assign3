UECM3033 Assignment #3 Report
========================================================

- Prepared by: Koe Wei Shiang
- Tutorial Group: T2

--------------------------------------------------------

## Task 1 --  Gauss-Legendre formula

The reports, codes and supporting documents are to be uploaded to Github at: 

https://github.com/jacksonkoe/UECM3033_assign3

Explain how you implement your `task1.py` here.

The weights and nodes used in Gauss-Legendre quadrature are computed using the interval [-1, 1]. Therefore, we must change the integral into [-1,1] from [a,b] when we want to apply the rule. The following code is used to make the change of integral and then find the approximation of the exact solution of the integral.

new_x = (b-a)*x/2 + ((b+a)/2)
summation = sum(w*f(new_x))
ans = ((b-a)/2)*summation

Finally, we obtain the approximation which is 0.400338097411.

Explain how you get the weights and nodes used in the Gauss-Legendre quadrature.

The weights and nodes used in the Gauss-Legendre quadrature are obtained using the code x,w = np.polynomial.legendre.leggauss(n).

---------------------------------------------------------

## Task 2 -- Predator-prey model

Explain how you implement your `task2.py` here, especially how to use `odeint`.

An ode system consisting of ode_system, y_initial, t and args=(a,b) is created where

(1)ode_system is a function which defines the set of differential equations
(2)y_initial is the initial value of y
(3)t is consisting of 101 points from t=0 to t=5 years
(4)args=(a,b) is the arguments that will be passed to the ode_system

The code "sol = odeint(ode_system,y_initial,t,args=(a, b))" is used to solve the differential equations.

Put your graphs here and explain.

https://github.com/jacksonkoe/UECM3033_assign3/blob/master/Graph_y0_y1_vs_t_0.1.jpg

y0 indicates the number of prey while y1 is the number of predators.
From the graph, we can see that the number of prey increases when the number of predator decreases as time goes on.

https://github.com/jacksonkoe/UECM3033_assign3/blob/master/Graph_y1_vs_y0_0.1.jpg

As we can notice, there is a inverse relationship between y0 and y1.

https://github.com/jacksonkoe/UECM3033_assign3/blob/master/Graph_y0_y1_vs_t_0.11.jpg

https://github.com/jacksonkoe/UECM3033_assign3/blob/master/Graph_y1_vs_y0_0.11.jpg

Basically for y0 = 0.11, the relationships of the both graphs render less difference compared to y0 = 0.1.

Is the system of ODE sensitive to initial condition? Explain.

From the initial value y0 = 0.1 and y0 = 0.11, we find out the changes of the graph are relatively small. We cannot get a different conclusion by looking at these graphs. Therefore, the system of ODE is said to be not sensitive to the initial condition.

-----------------------------------

<sup>last modified: 18th April 2016</sup>
