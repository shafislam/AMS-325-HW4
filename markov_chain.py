import numpy as np
import matplotlib.pyplot as plt

def markov_chain(n, N):
    p = np.empty([n, 1])
    p = p / np.linalg.norm(p, ord=1)
    P = np.empty([n, n])
    P = P / np.linalg.norm(P, ord=1)
    
    """creates normalized probability vector and array
    """
        
    w, v = np.linalg.eig(P.T)

    p_stationary = v[:,(np.argmax(w))]

    y_axis = []
    x_axis = np.linspace(0, N, N)
    while N > 0:
        y_axis += [np.linalg.norm(p - p_stationary)]
        p = (P.T @ p)
        N -= 1
        
    """creates array for y-axis of plot consisting of 
        the difference between p and p_stationary
    """
    
    plt.plot(x_axis, y_axis)
    plt.show()
    print(p)
    print(P)
