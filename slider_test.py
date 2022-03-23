import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button

#parameterized function
def f(tdr, val):
    return val * tdr

tdr = [np.linspace(1., 4., 6) for x in range(6)]

#initial parameter
init_time = 0

#fig and line to manipulate
fig, ax = plt.subplots()
line = plt.pcolormesh(tdr)

#adjust plot to make room for slider
plt.subplots_adjust(bottom=0.25)

left = 0.2
bottom = 0.1
width = 0.7
height = 0.02

#slider to control time step
ax_time = plt.axes([left, bottom, width, height])
time_slider = Slider(ax=ax_time,label='Time Step',valmin=0,valmax=5,valinit=init_time,valstep=1)

#function called when a slider value is changed
def update(val):
    #line.set_data(f(tdr, time_slider.val))
    plt.pcolormesh(f(tdr, int(time_slider.val)), axes=ax)
    fig.canvas.draw_idle()

#register the update function with the slider
time_slider.on_changed(update)

ax_reset = plt.axes([0.8, 0.025, 0.1, 0.04])
button = Button(ax_reset, 'Reset', hovercolor='0.9')

def reset(event):
    time_slider.reset()
button.on_clicked(reset)

plt.show()