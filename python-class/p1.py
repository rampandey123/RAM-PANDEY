
def linear_function(a,b):
	def inner(x):
		return a*x+b
	return inner

print(linear_function(2.,1.)(5.1))

f = linear_function(2.,1.)
print(f)
print(dir(f))	# list of attributes
print(f.__closure__)

############################

print(*[i**2 for i in range(10)])	# list comprehension, * - unpacking
print(*(i**2 for i in range(10)))	# generator expression
print(*map(lambda i:i**2,range(10)))
print(*filter(lambda i:i%2 == 0,range(10)))
print(sorted(range(-5,5),key=abs))

############################

from functools import wraps

def restriction(up,lo):
	def decorator(f):
		@wraps(f)
		def inner(*args):
			y = f(*args)
			if y > up: 	
				return up
			if y < lo: 	
				return lo
			else:		
				return y
		#inner.__name__ = f.__name__
		#inner.__doc__ = f.__doc__ 
		return inner
	return decorator

def derivative(f):
	h = 1e-5
	@wraps(f)
	def inner(x):
		return (f(x+h) - f(x))/h
	#inner.__name__ = f.__name__
	#inner.__doc__ = f.__doc__
	return inner

@restriction(.5,-.5)
@derivative
def f(x):
	"""Our quadratic function"""
	return x**2-2

"""
import numpy as np
import matplotlib.pyplot as plt

X = np.linspace(-2,2,201)
Y = [f(x) for x in X]
plt.plot(X,Y)
plt.show()
"""

print(f.__name__, f.__doc__)
print(str.strip.__doc__)
