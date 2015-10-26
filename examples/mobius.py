""" The standard S-Box used in Rijndael. """

from functools import partial

# Because the core is present
# in parent directory.
from sys import path
path.insert(1, '..')

import core
import analysis


def mobius_transform(z, a, b, c, d):
    numerator = core._multiply(a, z, reduced) ^ b
    denominator = core._multiply(c, z, reduced) ^ d
    return core._multiply(numerator, core.inverse(denominator, reduced), reduced)

reduced = core._B2I(core._I2B(0x11B)[1:])

# Partials are fun!
affine = partial(core.affine, u=0x1A, v=0x63)
power = partial(core.inverse, r=reduced)
mobius = partial(mobius_transform, a=33, b=23, c=12, d=9)

sbox = []

# Apply transformations on all element
for i in range(256):
    # sbox.append(mobius(i))
    sbox.append(affine(power(mobius(i))))

# The Box
print(core.pretty(sbox))
analysis.report(sbox)
