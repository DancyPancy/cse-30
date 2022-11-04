# create a rose curve in polar coordinates and
# add widgets that can control the curve parameters
# such as buttons and sliding bars

from matplotlib import pyplot as plt
from matplotlib.widgets import Slider, Button, RadioButtons
import numpy as np

def update(val):
    n = slider1.val
    d = slider2.val
    theta = np.linspace(0, d/n*16*np.pi, 600)
    r = np.cos(theta * n / d)
    ax.clear()
    ax.plot(theta+(r<0)*np.pi, np.abs(r), color='red')




# main
fig = plt.figure(figsize=(8,8))

ax = fig.add_subplot(1, 1, 1, polar=True)
ax.set_title("Rose Curve", pad = 20)

n, d = 3, 9
theta = np.linspace(0, d*2*np.pi, 600)
r = np.cos(theta * n / d)
line, = ax.plot(theta+(r<0)*np.pi, np.abs(r), color='red')

plt.subplots_adjust(left=0.25, bottom=0.25)
slider1_ax = plt.axes([0.25, 0.15, 0.65, 0.03])
slider2_ax = plt.axes([0.25, 0.1, 0.65, 0.03])
slider1 = Slider(slider1_ax,'n value',0,13,valinit=n,valfmt="%i", valstep=1)
slider2 = Slider(slider2_ax,'d value',1,12,valinit=d,valfmt="%i", valstep=1)
slider1.on_changed(update)
slider2.on_changed(update)

plt.show()