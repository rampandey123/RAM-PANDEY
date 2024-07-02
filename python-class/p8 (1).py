import numpy as np
from scipy.integrate import solve_ivp, odeint
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

G = 1; M = 1;

def vector_field(t,x):					# (t,x) for solve_ivp, (x,t) for odeint
	rx, ry, vx, vy = x					# phase space variables
	c = - G*M/(rx ** 2 + ry ** 2) ** 1.5			
	return [vx, vy, c*rx, c*ry]			# phase velocity

time_points = np.linspace(0,12,1001)
t_span = [time_points[0],time_points[-1]]
initial_condition = [.5,0,0,1]
res = solve_ivp(vector_field, t_span, initial_condition, t_eval = time_points,
				method = 'DOP853')
y = res.y.T
#y = odeint(vector_field,initial_condition,time_points)

# time series
#for i in range(4):
#	plt.plot(time_points,y[:,i])

#trajectory
#plt.plot(y[:,0],y[:,1])

fig = plt.figure()

trajectory, = plt.plot([initial_condition[0]],[initial_condition[1]])
earth, 		= plt.plot([initial_condition[0]],[initial_condition[1]],'g.',
						markersize = 10)
sun 		= plt.plot([0],[0],'y*',markersize=10)

def anim(i):
	earth.set_xdata(y[i,0])	# i-th rx
	earth.set_ydata(y[i,1])	# i-th ry
	trajectory.set_xdata(y[:i,0])	# from 0-th to i-th rx 
	trajectory.set_ydata(y[:i,1])	# from 0-th to i-th ry

a = FuncAnimation(fig,anim,range(len(time_points)),interval = 25)

plt.xlim(-.3,.7)
plt.ylim(-.5,.5)
plt.show()
