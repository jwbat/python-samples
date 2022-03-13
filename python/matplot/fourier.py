import matplotlib.pyplot as plt
import numpy as np

t = np.arange(256)
sp = np.fft.fft(np.sin(t))
freq = np.fft.fftfreq(t.shape[-1])


def plot_exp():
    fig, ax = plt.subplots(1)

    ax.plot(freq, sp.real, 'xkcd:pink', label='Fourier', linewidth=2)
    ax.grid(visible=True)
    ax.set_title('Fourier', fontsize=16, color='0.1')
    ax.set_xlabel('x values', fontsize=16, color='0.1')
    ax.set_ylabel('y values', fontsize=16 ,color='0.1')
    ax.legend(loc='lower right', fontsize='x-large')

    ax.tick_params(labelcolor='xkcd:dark grey blue')
    fig.set_facecolor('xkcd:grey')
    ax.set_facecolor('xkcd:almost black')

    plt.xticks(fontsize=16)
    plt.yticks(fontsize=16)
    plt.show()

plot_exp()
