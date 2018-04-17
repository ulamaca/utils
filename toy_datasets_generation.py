# Generating A Partial Swiss-Roll
import numpy as np
from sklearn.utils import check_random_state

def make_partial_swiss_roll(n_samples=100, noise=0.0, random_state=None):
    """stolen from sklearn"""
    generator = check_random_state(random_state)
    t = 1.5 * np.pi * (2 + (2/3) * generator.rand(1, n_samples)) # took data from 3-4pi
    x = t * np.cos(t)
    y = 21 * generator.rand(1, n_samples)
    z = t * np.sin(t)

    X = np.concatenate((x, y, z))
    X += noise * np.random.randn(3, n_samples)
    X = X.T
    t = np.squeeze(t)

    return X, t