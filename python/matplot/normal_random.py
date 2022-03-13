import matplotlib.pyplot as plt
import numpy as np

a = np.linspace(0, 2*np.pi, 500)
r = np.random.normal(loc=1.0, scale=0.2, size=500)
x = r * np.cos(a)
y = r * np.sin(a)

def plot_exp():
    fig, ax = plt.subplots(1)

    ax.plot(x, y, 'xkcd:golden yellow', label='circle', linewidth=2)
    ax.grid(visible=True)
    ax.set_title('Burst', fontsize=16, color='xkcd:dark orange')
    ax.set_xlabel('x values', fontsize=16, color='0.1')
    ax.set_ylabel('y values', fontsize=16 ,color='0.1')

    ax.tick_params(labelcolor='xkcd:dark orange')
    fig.set_facecolor('xkcd:dark grey')
    ax.set_facecolor('xkcd:almost black')

    plt.axis('scaled')
    plt.xticks(fontsize=16)
    plt.yticks(fontsize=16)
    plt.show()

plot_exp()
