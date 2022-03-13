'''
  Cross-correlation is a measure of similarity of two series as a function 
  of the displacement of one relative to the other. This is also known 
  as a sliding dot product or sliding inner-product. It is commonly 
  used for searching a long signal for a shorter, known feature. It 
  has applications in pattern recognition, single particle analysis,
  electron tomography, averaging, cryptanalysis, and neurophysiology.
  The cross-correlation is similar in nature to the convolution of two functions.
  In an autocorrelation, which is the cross-correlation of a signal with itself,
  there will always be a peak at a lag of zero, and its size will be the signal energy.
'''


import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3, 10, 500)
a = np.tan(x)
b = np.cos(x)
y = np.correlate(a, b, "same")


def plot_exp():
    fig, ax = plt.subplots(1) # facecolor='xkcd:almost black'

    ax.plot(x, y, 'xkcd:neon pink', label='correlate(tan, cos)', linewidth=3)

    ax.grid(visible=True)
    ax.set_title('Cross-correlation of tangent and cosine',
                  fontsize=16, color='xkcd:dark orange')
    ax.set_xlabel('x values', fontsize=16, color='0.1')
    ax.set_ylabel('y values', fontsize=16 ,color='0.1')
    ax.legend(loc='upper right', fontsize='x-large')

    ax.tick_params(labelcolor='xkcd:dark orange')
    fig.set_facecolor('xkcd:dark grey')
    ax.set_facecolor('xkcd:almost black')

    plt.xticks(fontsize=16)
    plt.yticks(fontsize=16)
    plt.show()

plot_exp()
