#!/usr/bin/python3

import numpy as np
import math

def angle_between(v1: np.ndarray, v2: np.ndarray):
    v1_u = v1 / np.linalg.norm(v1)
    v2_u = v2 / np.linalg.norm(v2)
    return np.arccos(np.clip(np.dot(v1_u, v2_u), -1.0, 1.0))

def randrange(a, b):
    """Random number between a and b."""
    return a + np.random.random() * (b - a)

def norm(vector):
    """Compute the norm of a vector."""
    return math.sqrt(vector[0]**2 + vector[1]**2)


def norm2(vector):
    """Compute the square norm of a vector."""
    return vector[0] * vector[0] + vector[1] * vector[1]


def dist2(a, b):
    """Return the square distance between two vectors.

    Parameters
    ----------
    a : np.array
    b : np.array
    """
    return norm2(a - b)


def dist(a, b):
    """Return the distance between two vectors.

    Parameters
    ----------
    a : np.array
    b : np.array
    """
    return norm(a - b)


def normalize(vector, pre_computed=None):
    """Return the normalized version of a vector.

    Parameters
    ----------
    vector : np.array
    pre_computed : float, optional
        The pre-computed norm for optimization. If not given, the norm
        will be computed.
    """
    n = pre_computed if pre_computed is not None else norm(vector)
    if n < 1e-13:
        return np.zeros(2)
    else:
        return np.array(vector) / n


def truncate(vector, max_length):
    """Truncate the length of a vector to a maximum value."""
    n = norm(vector)
    if n > max_length:
        return normalize(vector, pre_computed=n) * max_length
    else:
        return vector
