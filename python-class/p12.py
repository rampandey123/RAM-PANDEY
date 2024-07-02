import numpy as np
from time import time
import matplotlib.pyplot as plt

N = 2401
X = np.linspace(-2,1,N)
Y = np.linspace(-1.5,1.5,N)
X,Y = np.meshgrid(X,Y)

Z = X + 1j * Y

#print(Z)

def escape_index(z0):
	z=z0
	for n in range(255):
		if abs(z) > 2:
			return n
		z = z**2 + z0
	return 255

###### BAD
"""
t = time()
res = np.array([[escape_index(Z[i,j]) for j in range(N)] for i in range(N)])
print(time()-t)
"""
######

###### VERY BAD
"""
t = time()
res = np.zeros(Z.shape,dtype=int)
for i in range(N):
	for j in range(N):
		res[i,j] = escape_index(Z[i,j])
print(time()-t)
"""
######

###### BETTER
"""
@np.vectorize
def escape_index(z0):
	z=z0
	for n in range(255):
		if abs(z) > 2:
			return n
		z = z**2 + z0
	return 255

t = time()
res = escape_index(Z)
print(time()-t)
"""
######

def mandelbrot(Z):
	Z0 = np.copy(Z)
	res = 255*np.ones(Z.shape)
	for n in range(255):
		res[np.abs(Z)>2] = n	# res[np.logical_and(np.abs(Z)>2,res==255)] = n 
		Z = Z**2 + Z0
	return res

t = time()
res = mandelbrot(Z)
print(time()-t)

#############

M = 4
t = time()
parts = [Z[:,i*Z.shape[1]//M:(i+1)*Z.shape[1]//M] for i in range(M)]
results = map(mandelbrot,parts)
res = np.hstack(results)
print(time()-t)

##############

from multiprocessing import Pool

M = 4
t = time()
parts = [Z[:,i*Z.shape[1]//M:(i+1)*Z.shape[1]//M] for i in range(M)]
p = Pool()	# pool of subprocess, they can map a sequence
results = p.map(mandelbrot,parts)
res = np.hstack(results)
print(time()-t)


plt.imshow(res)
plt.show()
