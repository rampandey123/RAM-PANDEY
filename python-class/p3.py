class Vector:
	def __init__(self,x,y):
		self.x = x
		self.y = y
	def __str__(self):
		return f'[{self.x};{self.y}]'
	def __getattr__(self,name):	# handles not defined attributes
		if name == 'r':
			return (self.x**2+self.y**2)**.5
		else:
			raise AttributeError
	def __setattr__(self,name,value):
		if name == 'r':
			ratio = value / v.r
			self.x *= ratio
			self.y *= ratio
		else:
			super().__setattr__(name,value)	# we rever original behaviour of __setattr__


class Vector:
	def __init__(self,x,y):
		self.x = x
		self.y = y
	def __str__(self):
		return f'[{self.x};{self.y}]'
	#r = property(lambda self: (self.x**2+self.y**2)**.5)
	@property	# function property returns a descriptor
	def r(self):
		return (self.x**2+self.y**2)**.5
	@r.setter
	def r(self,value):
		ratio = value / v.r
		self.x *= ratio
		self.y *= ratio 


v = Vector(3,4)
print(hasattr(v,'r'), 'r' in dir(v))
print(v.r)
v.r = 10
print(v.x,v.y,v.r)
print(hasattr(v,'r'), 'r' in dir(v))
print(v.__dict__)
#del v.r

##############

class K:
	__x = 1				# pseudoprivate attribute
	def x(self):
		return self.__x

class Child(K):
	__x = 2

k = K()
#print(k.__x)
print(k.x())
print(K.__dict__)
print(k._K__x)
c = Child()
print(c.x())

##############

from math import pi, sin, cos

class Vector:
	__slots__ = ('x','y')
	def __init__(self,x,y):
		self.x = x
		self.y = y
	@staticmethod
	def norm(x,y):
		return (x**2+y**2)**.5
	@classmethod
	def polar(cls, r, phi):
		return cls(r*cos(phi),r*sin(phi))
	def __str__(self):
		return f'[{self.x};{self.y}]'
	@property	# function property returns a descriptor
	def r(self):
		return self.norm(self.x,self.y)
	@r.setter
	def r(self,value):
		ratio = value / v.r
		self.x *= ratio
		self.y *= ratio 

class Our_Vector(Vector):
	pass

v = Vector.polar(5, pi/2)			# here cls = Vector
print(v, type(v))
v.r = 10
#v.a = 1

v = Our_Vector.polar(5, pi/2)		# here cls = Our_Vector
print(v, type(v))
print(v.r)
print(dir(v))		# Our_vector has __slots__ AND __dict__
v.a = 1				# hence we again can add our attributes to instances

#################

from time import time
import tracemalloc as tm

class K:
	__slots__=('a')
	def __init__(self,a):
		self.a = a

tm.start()
t = time()

l = [K(i) for i in range(10**5)]

print('time: {}, actual memory: {}, peak memory: {}'.format(time()-t,
			*tm.get_traced_memory()))
tm.stop()

class K:
	def __init__(self,a):
		self.a = a

tm.start()
t = time()

l = [K(i) for i in range(10**5)]

print('time: {}, actual memory: {}, peak memory: {}'.format(time()-t,
			*tm.get_traced_memory()))
tm.stop()
