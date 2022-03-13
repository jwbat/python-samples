"""
Zip lists of points on two concentric circles.
Connect into a single line that spans them.
"""

import matplotlib.pyplot as plt
import numpy as np

a = np.linspace(0, 2*np.pi, 500)

x, y = np.cos(a), np.sin(a) # x, y coords of circle 1
p = list(zip(x, y))
p = p[0: 490 :4] # every other point on circle one

x2, y2 = 1.5 * x, 1.5 * y  # x, y coords of circle 2
q = list(zip(x2, y2))
q = q[10: 500 :4] # every other point circle two

m = list(zip(p, q))  # alternate the points on one with the points on two.
                     # m is list of tuples of (x, y) tuples.
m = [el for tup in m for el in tup]  # m is now a list of tuples (x, y).
x3 = [el[0] for el in m]
y3 = [el[1] for el in m]

def plot_exp():
    fig, ax = plt.subplots(1)

    ax.plot(x, y, 'xkcd:aqua', linewidth=2)
    ax.plot(x2, y2, 'xkcd:celadon', linewidth=2)
    ax.plot(x3, y3, 'xkcd:orangish red', linewidth=2)

    # ax.grid(b=True)
    ax.set_title('Two Circles',
                  fontsize=16, color='xkcd:dark orange')
    ax.set_xlabel('x values', fontsize=16, color='0.1')
    ax.set_ylabel('y values', fontsize=16 ,color='0.1')
    # ax.legend(loc='upper right', fontsize='x-large')

    ax.tick_params(labelcolor='xkcd:dark orange')
    fig.set_facecolor('xkcd:dark grey')
    ax.set_facecolor('xkcd:almost black')

    plt.axis('scaled')
    plt.xticks(fontsize=16)
    plt.yticks(fontsize=16)
    plt.show()

plot_exp()
