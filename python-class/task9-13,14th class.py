import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

N = 2401
X = np.linspace(-2, 1, N)
Y = np.linspace(-1.5, 1.5, N)
X, Y = np.meshgrid(X, Y)
Z = X + 1j * Y
max_iter = 255

def mandelbrot_animation(Z, max_iter=255):
    Z0 = np.copy(Z)
    res = np.zeros(Z.shape, dtype=int)
    for n in range(max_iter):
        mask = np.abs(Z) <= 2
        res[mask] = n
        Z[mask] = Z[mask]**2 + Z0[mask]
        yield res

fig, ax = plt.subplots()
cax = ax.imshow(np.zeros(Z.shape), interpolation='nearest', cmap='hot', vmin=0, vmax=max_iter - 1)
ax.set_title('Mandelbrot Set Animation')

def update(frame):
    cax.set_array(frame)
    return [cax]

ani = animation.FuncAnimation(fig, update, frames=mandelbrot_animation(Z, max_iter), blit=True, repeat=False)
plt.show()
