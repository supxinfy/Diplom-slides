import numpy as np

import matplotlib.pyplot as plt
import matplotlib.colors as colors

import functools
import matplotlib.colors as colors


@functools.cache
def MW(n, p):

    if n == 0:
        return np.array([1])
    
    mw = np.array(
        [[1, 1],
        [1, -1]]
    )

    for i in range(1, n):
        mw = np.pad(mw, [(0, 1), (0, 1)]) + np.pad(mw, [(1, 0), (0, 1)]) + np.pad(mw, [(0, 1), (1, 0)]) - np.pad(mw, [(1, 0), (1, 0)])

        mw[:, 1:-1] = mw[:, 1:-1] * (p+1)//2

        mw = np.mod(mw, p)

    return np.mod(mw, p)


def hrbr(m, p):

    hr = lambda x: 0.77 if 0 <= x < 0.5 else 0.414
    br = lambda x: 5 * x + 0.5 if 0 <= x < 0.1 else -5 * x + 5.5 if 0.9 < x <= 1 else 1

    return np.round(255 * colors.hsv_to_rgb((hr(m/p) * (1 - m/p), 1, br(m / p))))

def MWplot(n, p):    
    mw = MW(n, p)

    hsv_mw = np.zeros((n+1, n+1, 3))
    for i in range(n+1):
        for j in range(n+1):
            hsv_mw[i][j] = hrbr(mw[i][j], p)
    return hsv_mw