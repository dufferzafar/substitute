""" The standard S-Box used in Rijndael. """

import core

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

# Yay!
print(core.pretty(sbox))
