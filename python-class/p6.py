import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

T = np.linspace(0,2*np.pi,1001)
X = np.sin(2*T)
Y = np.sin(3*T)

def update(phi):
	X = np.sin(2*T+phi)
	Y = np.sin(3*T+phi)
	l.set_xdata(X)
	l.set_ydata(Y)

fig,ax = plt.subplots()
l, = ax.plot(X,Y)
slider = Slider(ax = fig.add_axes([0.07,0.02,0.86,0.02]),
				label = r'$\phi$', valmin=-np.pi, valmax=np.pi,
				valinit=0)
slider.on_changed(update)

plt.show()
