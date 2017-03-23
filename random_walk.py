import numpy as np
from matplotlib import pyplot as plt

def random_walk(k_steps):
    delta_X = np.random.normal(0, 1, (2, k_steps))
    X_0 = np.array(([0.], [0.]))
    X_c = np.cumsum(delta_X, axis=1)
    X = np.concatenate((X_0, X_c), axis=1)
    return X
    
def draw_walk(X):
    plt.plot(X[0], X[1], 'ro-')
    plt.show()

if __name__ == '__main__':
    rw = random_walk(1000)
    draw_walk(rw)
