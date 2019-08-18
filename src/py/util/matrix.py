import numpy as np


def flipdiag(x, dim):
    a = np.zeros((dim, dim))
    for i in range(-1 * dim, dim):
        hd = x.diagonal(offset=i)
        a[i][0:len(hd)] = hd
    return a


def groups(x, size, start=0):
    return np.vstack([x[:, n:n + size] for n in range(start, x.shape[0] - size + 1) if len(x[n]) >= size])