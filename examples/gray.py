""" Gray/Hadamard Codes in the AES S-Box. """

from functools import partial
import numpy as np

# Because the core is present
# in parent directory.
from sys import path
path.insert(1, '..')

import core

from analysis import (
    differential_probability,
    # non_linearity,
    algebraic_degree
)


def binary_code(num, m):
    bits = core._I2B(num, fixed_length=8, reverse=True)
    # print(bits)
    bits = np.array(bits, ndmin=2)
    # print(bits.T)
    product = (m * bits.T) % 2
    # print(product.T.tolist()[0])
    return core._B2I(product.T.tolist()[0])

# Standard parameters
irreducible_polynomial = 0x11B
constant = 0x63

reduced = core._B2I(core._I2B(irreducible_polynomial)[1:])

# Binary hadmard matrix of size 8
hmatrix = [[1, 1, 1, 1, 1, 1, 1, 1],
           [1, 0, 1, 0, 1, 0, 1, 0],
           [1, 1, 0, 0, 1, 1, 0, 0],
           [1, 0, 0, 1, 1, 0, 0, 1],
           [1, 1, 1, 1, 0, 0, 0, 0],
           [1, 0, 1, 0, 0, 1, 0, 1],
           [1, 1, 0, 0, 0, 0, 1, 1],
           [1, 0, 0, 1, 0, 1, 1, 0]]

gmatrix = [[1, 1, 0, 0, 0, 0, 0, 0],
           [0, 1, 1, 0, 0, 0, 0, 0],
           [0, 0, 1, 1, 0, 0, 0, 0],
           [0, 0, 0, 1, 1, 0, 0, 0],
           [0, 0, 0, 0, 1, 1, 0, 0],
           [0, 0, 0, 0, 0, 1, 1, 0],
           [0, 0, 0, 0, 0, 0, 1, 1],
           [0, 0, 0, 0, 0, 0, 0, 1]]


# Partials are fun!
affine = partial(core.affine, c=constant)
power = partial(core.inverse, r=irreducible_polynomial)
hadamard = partial(binary_code, m=np.mat(hmatrix))
gray = partial(binary_code, m=np.mat(gmatrix))

# print(gray(15))

sbox = []

# Apply transformations on all element
for i in range(256):
    # sbox.append(affine(power(hadamard(i))))
    sbox.append(affine(power(gray(i))))

# The Box
print(core.pretty(sbox))

# Analysis
print("Differential Probability: %d" % differential_probability(sbox))
# print("Non Linearity: %d" % non_linearity(sbox))
print("Algebraic Degree: %d" % algebraic_degree(sbox))
