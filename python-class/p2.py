
class K:	# factory of instances
	x = 0
	def f(self,*args):
		print(args)
	

k1 = K()	#instance
k2 = K()

print(dir(k1))	

k1.x = 1
k2.y = 2
x = 3

print(dir(k1))

print(k1.x, k2.x, x)	# k2 has no x, but inherits it from K

K.f('Alice')
k2.f('Alice')
print(type(K.f),type(k2.f))

#############

print('X'+' Alice '.strip()+'X')
print(*map(lambda s:s.strip(),['a ', ' b', ' c ']))
# instance.strip() <=> class.strip(instance)
print('a'.__class__)
print(*map(str.strip,['a ', ' b', ' c ']))

############## constructor

class K:
	def __init__(self,x,y):
		self.x = x
		self.y = y

k = K(1,2)
print(k.x,k.y)

############## inheritance

class Parent:
	a = 2
	def function1(self):
		return self.a**2
	def function2(self):
		return 4*self.a

class Child(Parent):
	def function2(self):
		return 3*self.a

c = Child()
print(c.function1())
print(c.function2())

print(dir(c))

print(c.__class__ == Child)
print(c.__class__ == Parent)
print(isinstance(c,Child))
print(isinstance(c,Parent))

#################

class Vector:
	def __init__(self,x,y):
		self.x = x
		self.y = y
	def __str__(self):
		return f'[{self.x};{self.y}]'
	def __add__(self,other):
		return Vector(self.x+other.x,self.y+other.y)
	def __mul__(self,other):
		if isinstance(other,Vector):
			return self.x*other.x+self.y*other.y
		else:
			return Vector(self.x*other,self.y*other)
	__rmul__ = __mul__
	def __truediv__(self,other):
		if isinstance(other,Vector):
			raise TypeError('Cannot divide vector by vector')
		else:
			return Vector(self.x/other,self.y/other)
	__call__ = __mul__
	def __getitem__(self,item):
		if item == 'x':
			return self.x
		elif item == 'y':
			return self.y
		else:
			raise ValueError
	def __eq__(self,other):
		return self.x==other.x and self.y==other.y
	def __getattr__(self,name):	# handles not defined attributes
		if name == 'r':
			return (self.x**2+self.y**2)**.5
		else:
			raise AttributeError

v = Vector(-3,4)
print(v+v, v*v, v*2, 2*v, v/2) # v/v
print(dir(1))
print(9//4, 9%4, 9/4)
print(callable(v))
print(v(v))
print(v['x'])
print(v == Vector(-3,4))
print(7 & 3)

##########

# __sub__, __neg__, __neq__, __ge__, __gt__, __le__, __lt__, __and__
# @ = __matmul__

import numpy as np
x = np.array([1,2,3])
y = np.array([4,5,6])
print(x*y, x @ y)
print(dir(x))

def g():		# iterator defined as a value of generator function
	yield 1
	yield 2

print(g())
gen = g()
for i in gen:
	print(i)

gen = g()
print(next(gen),next(gen))
print(dir(gen))

class Our_range:
	def __init__(self,n):
		self.i=0
		self.n=n
	__iter__ = lambda self:self
	def __next__(self):
		i = self.i
		self.i += 1
		if i < self.n:
			return i
		else:
			raise StopIteration

def our_range(n):
	i = 0
	while i<n:
		yield i
		i+=1 

for i in our_range(5):
	print(i)

#######################

print(v,v.r)
v.y=0
print(v,v.r)	# does not update :(
print(v.unicorn)
