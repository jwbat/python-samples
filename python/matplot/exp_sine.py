import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 5, 500)

ysin = np.exp(-x) * np.sin(4*x) * np.cos(x)
ycos = np.exp(-x) * np.cos(4*x) * np.sin(x)

def plot_exp():
    fig, ax = plt.subplots(1) # facecolor='xkcd:almost black'

    ax.plot(x, ysin, 'xkcd:lime', label='exp(-x)*sin(4x)', linewidth=3)
    ax.plot(x, ycos, 'xkcd:magenta', label='exp(-x)*cos(4x)', linewidth=3)
    ax.grid(visible=True)
    ax.set_title('exp x sine functions', fontsize=16, color='0.1')
    ax.set_xlabel('x values 0 to 5', fontsize=16, color='0.1')
    ax.set_ylabel('y values', fontsize=16 ,color='0.1')
    ax.legend(loc='upper right', fontsize='x-large')

    ax.tick_params(labelcolor='xkcd:dark grey blue')
    fig.set_facecolor('xkcd:grey')
    ax.set_facecolor('xkcd:almost black')

    plt.xticks(fontsize=16)
    plt.yticks(fontsize=16)
    plt.show()

plot_exp()
