import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3, 10, 500)
y1 = np.sqrt(abs(x))
a = np.sin(x)
y2 = np.exp(a)
# y = np.convolve(a, a2, mode='same')

def plot_exp():
    fig, ax = plt.subplots(1)

    ax.plot(x, y1, 'xkcd:lemon', label='sqrt', linewidth=3)
    ax.plot(x, y2, 'xkcd:bright teal', label='exp(sin(x))', linewidth=3)
    ax.grid(visible=True)
    ax.set_title('f(x) = sqrt(|x|) & g(x) = exp(sin(x))',
                  fontsize=18, color='xkcd:dark orange')
    ax.set_xlabel('x values', fontsize=16, color='0.1')
    ax.set_ylabel('y values', fontsize=16 ,color='0.1')
    ax.legend(loc='lower right', fontsize='x-large')

    ax.tick_params(labelcolor='xkcd:dark orange')
    fig.set_facecolor('xkcd:dark grey')
    ax.set_facecolor('xkcd:almost black')

    plt.xticks(fontsize=16)
    plt.yticks(fontsize=16)
    plt.show()

plot_exp()
