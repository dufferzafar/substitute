""" Core functions used while creating S-Boxes. """


from functools import reduce


def _I2B(I, fixed_length=None, reverse=False):
    """ Convert an integer into a bit list. """
    if reverse:
        # LSB first form
        result = [int(bit) for bit in reversed(bin(I)[2:])]
        if fixed_length:
            while len(result) < fixed_length:
                result.append(0)
    else:
        result = [int(bit) for bit in bin(I)[2:]]
        if fixed_length:
            while len(result) < fixed_length:
                result.insert(0, 0)
    return result


def _B2I(B, reverse=False):
    """ Convert a bit list into a integer. """
    if reverse:
        return reduce(lambda x, y: (x << 1) + y, list(reversed(B)))
    else:
        return reduce(lambda x, y: (x << 1) + y, B)


def _add(a, b):
    """ Add two numbers by xor-ing them bitwise. """

    # Todo: What if numbers have bigger length than 8
    a = _I2B(a, fixed_length=8)
    b = _I2B(b, fixed_length=8)
    return _B2I([i ^ j for i, j in zip(a, b)])


def _multiply(a, b, r):
    """
    Multiply two numbers in a finite field.

    Uses a reduced value of the irreducible polynomial.
    """
    p = 0
    while b:
        if b & 1:
            p ^= a
        b >>= 1
        a <<= 1
        if a & 256:
            a ^= r
    return p & (256 - 1)


def inverse(num, r):
    """ Find inverse of an element by Brute-force approach. """
    if int(num) == 0:
        return 0
    else:
        # Multiply with every number in the field and
        # check if the result is one. Easy Peasy!
        # Todo: Use Extended Euclidean Algo
        # or Logs/Anti-Logs
        for i in range(1, 256):
            if _multiply(num, i, r) == 1:
                return i


def affine(a, u, v):
    """
    Affine Transformation.

    b(x) = u(x) * a(x) + v(x)

    http://www.ijicic.org/ijicic-10-01041.pdf
    """

    return _add(_multiply(a, u, 257), v)


def pretty(sbox, border=True):
    """ Return a pretty printed SBox. """

    p = ''
    if border:
        # List of Columns
        p += '     '
        for i in range(16):
            p += '%02x' % i + ' '
        p += '\n'

        for i in range(52):
            p += '-'
        p += '\n'

    # Row
    for i in range(16):
        if border:
            p += '%02x' % i + ' | '

        # Entries
        for j in range(16):
            p += '%02x' % sbox[16*i+j] + ' '
        p += '\n'

    return p.upper()
