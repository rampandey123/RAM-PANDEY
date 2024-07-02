from scipy.integrate import quad
import numpy as np

print(quad(lambda x:x**2, 0,1))	# quad (function, lower_limit, upper_limit)
print(quad(lambda x:np.exp(-x**2), -np.inf, 0))
print(np.pi**.5/2)

print(quad(lambda x: quad(lambda y:x*y, 0, x)[0], 0, 1))
