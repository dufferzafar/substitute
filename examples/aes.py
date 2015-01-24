""" The standard S-Box used in Rijndael. """

# Because the core is present
# in parent directory.
from sys import path
path.insert(1, '..')

import core

from analysis import (
    differential_probability,
    non_linearity,
    algebraic_degree
)

# Standard parameters
irreducible_polynomial = 0x11B
affine_constant = 0x63

# A reduced version of a polynomial is an integer
# with the MSB cleared So, 0x11B becomes 0x1B and
# 0x169 becomes 0x69.
# These are used during multiplication
# Todo: Understand these completely.
reduced = core._B2I(core._I2B(irreducible_polynomial)[1:])

sbox = []

# Apply transformations on all element
for i in range(256):
    sbox.append(core.affine(core.inverse(i, reduced), affine_constant))

# The Box
print(core.pretty(sbox))

# Analysis
print("Differential Probability: %d" % differential_probability(sbox))
# print("Non Linearity: %d" % non_linearity(sbox))
print("Algebraic Degree: %d" % algebraic_degree(sbox))
