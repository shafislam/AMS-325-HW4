import numpy as np
import matplotlib.pyplot as plt

def mandelbrot(n, N_max, threshold):
    x = np.linspace(-2, 1, n)
    y = np.linspace(-1.5, 1.5, n)
    """creates two arrays corresponding to the x and y axes
    """
    c = x[:,newaxis] + 1j*y[newaxis,:]
    z = c
    mask = np.empty([1, 7])
    
    for c, i in zip(C_array, range(N_max)):
        z_var = z**2 + c
        mask[0][i] = (abs(z_var) < threshold)
        
    """creates an array for plot consisting of boolean
        values that correspond to whether or not the 
        z-value of a coordinate is less than the threshold
        value
    """
    
    plt.imshow(mask.T, extent = [-2, 1, -1.5, 1.5])
    plt.gray()
    plt.savefig('mandelbrot.png')

