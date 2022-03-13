import matplotlib.pyplot as plt
import numpy as np

t = np.linspace(-1.5, 1.5, 500)
y = np.cos(6 * np.pi * t) * np.exp(-np.pi * np.square(t))

def plot_exp():
    fig, ax = plt.subplots(1)

    ax.plot(t, y, 'xkcd:vibrant purple', linewidth=4)
    ax.grid(visible=True)
    ax.set_title('f(t) = cos(6πt) * exp(−πt^2)',
                  fontsize=18, color='xkcd:dark orange')
    ax.set_xlabel('t', fontsize=20, color='0.5')
    ax.set_ylabel('f(t)', fontsize=20 ,color='0.5')
    # ax.legend(loc='lower right', fontsize='large')

    ax.tick_params(labelcolor='xkcd:dark orange')
    fig.set_facecolor('xkcd:dark grey')
    ax.set_facecolor('xkcd:almost black')

    plt.xticks(fontsize=16)
    plt.yticks(fontsize=16)
    plt.show()

plot_exp()
