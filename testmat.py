import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation
def animate(i):
    line.set_ydata(np.sin(x+i/10.0))
    return line,
def init():
    line.set_ydata(np.sin(x))
    return line

# x = np.arange(1,11)
# y=x*3+4
# plt.plot(x,y)
# plt.show()
fig,ax = plt.subplots()
x = np.arange(0,2*np.pi,0.01)
line, = ax.plot(x,np.sin(x))

ani = animation.FuncAnimation(
    fig=fig,
    func=animate,
    frames=100,
    init_func=init,
    interval=20,
    blit=False
)
plt.show()
