import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

def vector_field(t,x):
	alpha, omega = x
	return [omega, -np.sin(alpha)]

time_points = np.linspace(0,10,101)
t_span = [time_points[0],time_points[-1]]
initial_condition = [.9*np.pi,0]
res = solve_ivp(vector_field, t_span, initial_condition, t_eval = time_points)

#plt.plot(res.t,res.y[0])
#plt.plot(res.t,res.y[1])
plt.plot(*res.y)
plt.show()
