"""
An Improved AES S-box And Its Performance Analysis
by Jie Cui et. al.

http://www.ijicic.org/ijicic-10-01041.pdf
"""

from functools import partial
from os.path import abspath, dirname

# Because the core is present in parent directory.
from sys import path
path.insert(1, dirname(dirname(abspath(__file__))))

import core
import analysis

reduced = core._B2I(core._I2B(0x11B)[1:])

affine = partial(core.affine, u=0x5B, v=0x5D)
power = partial(core.inverse, r=reduced)

sbox = []

for i in range(256):
    sbox.append(affine(power(affine(i))))

print(core.pretty(sbox))
analysis.report(sbox)
