import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig, ax = plt.subplots()

t = np.arange(0, 2*np.pi, 0.01)
line, = ax.plot(np.cos(t), np.sin(t))


def animate(i):
    line.set_ydata(np.sin(t))
    line.set_xdata(np.cos(t+i/10))
    print(i)
    return line,


ani = animation.FuncAnimation(
    fig, animate, interval=10, save_count=50)


plt.show()
