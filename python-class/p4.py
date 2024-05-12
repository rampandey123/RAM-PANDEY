import numpy as np
import matplotlib.pyplot as plt

A = np.array([1,2,3])
print(A)
A = np.linspace(0,1,11)
print(A)
A = np.arange(0,2,.33)
print(A)
A = np.zeros(5)
print(A)
A = np.ones(5)
print(A)

###############pointwise operations:

A = np.array([1,2,3])
B = np.array([4,5,6])
print(A+B, A*B, A**B, A / B)
print(A**.5, 2**A)
print(np.sin(A), np.log2(A))

print(np.logical_and(A>2,A<4))	# logical_or, ...

###############multidimensional arrays:

A = np.array([[1,2],[3,4]])
print(A)
print(A.shape)
A = np.zeros((2,2,2))
print(A, A.shape)

X = np.array([1,2,3])
Y = np.array([4,5,6])
X,Y = np.meshgrid(X,Y)
print(X)
print(Y)

Z = X**2 + Y**2

print(Z)

############# slices

A = np.arange(16,dtype=np.float).reshape(4,4)
#A = A.flatten()
print(A)
print(A[1:3,:])
print(A[:,:2])

A[1:3,1:3] = np.array([.1,.2,.3,.4]).reshape(2,2)
print(A)

A[A>10] = 0
print(A)

print(A/0)

############ linear algebra

print(dir(np.linalg))

sigma = np.array([[0,1+1j],[1-1j,0]])
spectr, eig_vect = np.linalg.eigh(sigma)
print(eig_vect @ np.diag(spectr) @ eig_vect.T.conjugate())

############ 2d-plotting

"""
X = np.linspace(-2,2,21)
plt.plot(X, X**2, 'r', marker = '*', markerfacecolor = 'b', label = r'$y = x^2$')
plt.legend()
plt.show()
"""

"""
X = np.linspace(-2,2,1001)
Y = 1/(X**2 - 1)
Y[np.abs(Y)>50] = np.NaN
plt.plot(X,Y)
plt.plot([1,1],[-50,50],'--r')
plt.plot([-1,-1],[-50,50],'--r')
plt.show()
"""

"""
T = np.linspace(0,2*np.pi,10001)
plt.plot(np.cos(3*T),np.sin(4*T+.4))
plt.show()
"""

########### 3d-ploting

"""
X = Y = np.linspace(-2,2,401)
X,Y = np.meshgrid(X,Y)
Z = X**2 + Y**2
#Z[Z<0.1] = np.NaN
#plt.contourf(X,Y,Z,50,cmap='jet') # contour, summer, winter
#plt.imshow(Z,extent=[-2,2,-2,2])
#plt.axis('equal')
#plt.show()

#%matplotlib - for jupyter
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = plt.axes(projection='3d', azim = 60, elev = 60)
ax.plot_surface(X,Y,Z,cmap='jet')
plt.savefig('figure.png')
plt.show()
"""

########### animation

from matplotlib.animation import FuncAnimation

fig = plt.figure()

X = np.linspace(-2,2,201)
Y = X**2
line, = plt.plot(X,Y)	# unpacking 1-element tuple

def anim(p):
	Y = X**2 - p*X**4
	line.set_ydata(Y)

a = FuncAnimation(fig, anim, np.arange(0,1,.01), repeat=False, interval = 50)
plt.show()
