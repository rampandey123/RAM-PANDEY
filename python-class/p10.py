from scipy.optimize import minimize
import numpy as np
import matplotlib.pyplot as plt

xa = 0; xb = 3
ya = 0; yb = 1

N = 100
x = np.linspace(xa,xb,N+1)
y = np.linspace(ya,yb,N+1)
dx = (xb-xa)/N

def one_step_time(a):
	y1,y2 = a
	return (dx**2 + (y1-y2)**2)**.5 / (y1**.5 + y2**.5)

def travel_time(y: 'internal points'):
	Y = np.zeros((y.shape[0]+1,2))
	Y[0,0] = ya
	Y[1:,0] = y
	Y[:-1,1] = y
	Y[-1,1] = yb
	return sum(map(one_step_time,Y)) #[f(a) for a in Y]

res = minimize(travel_time,y[1:-1])
print(res)

y[1:-1] = res.x
plt.plot(x,-y,'.-')
plt.show()
