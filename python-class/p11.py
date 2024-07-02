from scipy.optimize import minimize
import numpy as np
import matplotlib.pyplot as plt

xa = 0; xb = 3
ya = 0; yb = 1
L=4

N = 40
x = np.linspace(xa,xb,N+1)
y = np.linspace(ya,yb,N+1)
dx = (xb-xa)/N

def one_segment_energy(a):
	y1,y2=a
	return ((y1-y2)**2+dx**2)**.5*(y1+y2)/2

def chain_energy(y):
	Y = np.zeros((y.shape[0]+1,2))
	Y[0,0] = ya;	Y[1:,0] = y;	Y[:-1,1] = y;	Y[-1,1] = yb
	return sum(map(one_segment_energy,Y))

def one_segment_length(a):
	y1,y2=a
	return ((y1-y2)**2+dx**2)**.5
	
def chain_lenght_diff(y):
	Y = np.zeros((y.shape[0]+1,2))
	Y[0,0] = ya;	Y[1:,0] = y;	Y[:-1,1] = y;	Y[-1,1] = yb
	return sum(map(one_segment_length,Y)) - L

res = minimize(chain_energy,y[1:-1],method='SLSQP',
			constraints={'type':'eq','fun':chain_lenght_diff},
			options={'maxiter':200})
print(res)

def new_function(y):
	return chain_energy(y) + K*chain_lenght_diff(y)**2

K = 1e5
res = minimize(new_function,y[1:-1])
print(res)

y[1:-1] = res.x

from scipy.optimize import curve_fit

def cosh(x,a,b,c,d):
	return c*np.cosh((x-a)/b)+d

res = curve_fit(cosh,x,y)
a,b,c,d = res[0]

plt.plot(x,y,'.-')
plt.plot(x,cosh(x,a,b,c,d))
plt.show()
