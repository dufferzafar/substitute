""" The standard S-Box used in Rijndael. """

from functools import partial

# Because the core is present
# in parent directory.
from sys import path
path.insert(1, '..')

import core

from analysis import (
    differential_probability,
    is_bijective,
)

# Standard parameters
irreducible_polynomial = 0x11B
constant = 0x63

reduced = core._B2I(core._I2B(irreducible_polynomial)[1:])


def mobius_transform(z, a, b, c, d):
    numerator = core._multiply(a, z, reduced) ^ b
    denominator = core._multiply(c, z, reduced) ^ d
    return core._multiply(numerator, core.inverse(denominator, reduced), reduced)

# Partials are fun!
affine = partial(core.affine, c=constant)
power = partial(core.inverse, r=irreducible_polynomial)
mobius = partial(mobius_transform, a=33, b=23, c=12, d=9)

sbox = []

# Apply transformations on all element
for i in range(256):
    sbox.append((mobius(i)))
    # sbox.append(affine(power(mobius(i))))

# The Box
print(core.pretty(sbox))

# Analysis
print("Differential Probability: %d" % differential_probability(sbox))
print("Is Bijective? " + str(is_bijective(sbox)))
