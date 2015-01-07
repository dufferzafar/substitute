"""
Generate new (and improved?) S-Boxes.

By testing out different irreducible polynomials and affine constants.
"""

import core

# A list of irreducible polynomials and constants
# http://www.sciencedirect.com/science/article/pii/S2212017313006051
irreducibles = [0x11B, 0x11D, 0x12B, 0x12D, 0x139, 0x13F, 0x14D, 0x15F, 0x163,
                0x165, 0x169, 0x171, 0x177, 0x17B, 0x187, 0x18B, 0x18D, 0x19F,
                0x1A3, 0x1A9, 0x1B1, 0x1BD, 0x1C3, 0x1CF, 0x1D7, 0x1DD, 0x1E7,
                0x1F3, 0x1F5, 0x1F9]

constants = [0X0A, 0X0F, 0X15, 0X2A, 0X2B, 0X31, 0X32, 0X35, 0X38, 0X40, 0X4A,
             0X4E, 0X54, 0X5E, 0X62, 0X6E, 0X74, 0X7E, 0XF5, 0XF0, 0XEA, 0XD5,
             0XCE, 0XCD, 0XCA, 0XC7, 0XBF, 0XB5, 0XB1, 0XAB, 0XA1, 0X9D, 0X91,
             0XDB, 0X81]

for p in irreducibles:
    reduced = core._B2I(core._I2B(p)[1:])

    for c in constants:

        sbox = []

        for elem in range(256):
            sbox.append(core.affine(core.inverse(elem, reduced), c))

    print("Polynomial: %s, Constant: %s " % (hex(p).upper(), hex(c).upper()))
    print(core.pretty(sbox))
