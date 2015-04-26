"""
Non Linearity of an SBox.

Todo: Needs to be tested on sample boxes.
"""

import math
from core import _I2B


def _fwt(f):
    """
    Fast Walsh Hadamard Transform.

    f is a Boolean function represented as a TT of length 2^n
    """

    # Conert 0/1 based truth table to 1/-1 based
    wf = []
    for x in f:
        if x == 0:
            wf.append(1)
        else:
            wf.append(-1)

    order = len(f)  # k = 2^n
    size = order // 2

    while size >= 1:
        left = 0
        while left < order - 1:
            for p in range(size):
                right = left + size
                a, b = wf[left], wf[right]
                wf[left] = a + b
                wf[right] = a - b
                left = left + 1
            left = right + 1
        size = size // 2

    return wf


def _nl(f):
    """ Non Linearity of a Boolean Function. """
    n = int(math.log(len(f), 2))
    fw = [abs(i) for i in _fwt(f)]
    x = ((2 ** (n - 1)) - (max(fw) / 2))
    return x


def non_linearity(sbox):
    """ Non Linearity of a SBox. """

    # Create a bit matrix of all the entries in the box
    #
    # Columns of this matrix represents the eight boolean
    # functions that constitute this sbox.
    bit_matrix = []
    for num in sbox:
        bit_matrix.append(_I2B(num, fixed_length=8))

    nonlin = []
    for i in range(8):
        # Take the ith column of the matrix
        column = [row[i] for row in bit_matrix]
        nonlin.append(_nl(column))

    # Todo: Is it min or max?
    return min(nonlin)
