""" The standard S-Box used in Rijndael. """

from functools import partial
from os.path import abspath, dirname

# Because the core is present in parent directory.
from sys import path
path.insert(1, dirname(dirname(abspath(__file__))))

import core
import analysis

# A reduced version of a polynomial is an integer
# with the MSB cleared So, 0x11B becomes 0x1B and
# 0x169 becomes 0x69.
# These are used during multiplication
# Todo: Understand these completely.
reduced = core._B2I(core._I2B(0x11B)[1:])

affine = partial(core.affine, u=0x1F, v=0x63)
power = partial(core.inverse, r=reduced)

sbox = []

# Apply transformations on all elements
for i in range(256):
    sbox.append(affine(power(i)))

# The Box
print(core.pretty(sbox))
analysis.report(sbox)
