
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, FFMpegWriter
from mpl_toolkits.mplot3d import Axes3D

X = Y = np.linspace(-4,4,1001)
X,Y = np.meshgrid(X,Y)
Z = np.sin(X+Y)

fig = plt.figure()
ax = plt.axes(projection='3d', azim = 60, elev = 60)
ax.plot_surface(X,Y,Z,cmap='jet')

def anim(phi):
	Z = np.exp(-.1*phi)*np.sin(X+Y+phi)
	ax.clear()
	ax.set_zlim(-1,1)
	ax.plot_surface(X,Y,Z,cmap='jet')

a = FuncAnimation(fig,anim,np.arange(0,2*np.pi,.1))

from IPython.display import HTML
HTML(a.to_html5_video())

#writervideo = FFMpegWriter(fps=2)
#a.save('our_wave.mp4',writer = writervideo)

plt.show()
