""" Core functions used while creating S-Boxes. """


from functools import reduce


def _I2B(I, fixed_length=None, reverse=False):
    """ Convert an integer into a bit list. """
    if reverse:
        result = [int(bit) for bit in reversed(bin(I)[2:])]
        if fixed_length:
            while len(result) < fixed_length:
                result.append(0)
    else:
        result = [int(bit) for bit in bin(I)[2:]]
    return result


def _B2I(B, reverse=False):
    """ Convert a bit list into a integer. """
    if reverse:
        return reduce(lambda x, y: (x << 1) + y, list(reversed(B)))
    else:
        return reduce(lambda x, y: (x << 1) + y, B)


def multiply(a, b, reduced):
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
            a ^= reduced
    return p & (256 - 1)


def inverse(num, reduced):
    """ Find inverse of an element by Brute-force approach. """
    if int(num) == 0:
        return 0
    else:
        # Multiply with every number in the field and
        # check if the result is one. Easy Peasy!
        # Todo: Use Extended Euclidean Algo
        # or Logs/Anti-Logs
        for i in range(1, 256):
            if multiply(num, i, reduced) == 1:
                return i


def affine(b, c):
    """ Affine Transformation. """
    # Convert the integers to a list of bits
    # each of length 8, in LSB first form.
    # So, 13 becomes [1, 0, 1, 1, 0, 0, 0, 0]
    b, c, d = _I2B(b, 8, True), _I2B(c, 8, True), _I2B(b, 8, True)

    # Apply the affine transformation
    for i in range(8):
        d[i] ^= b[(i+4) % 8] ^ b[(i+5) % 8] ^ b[(i+6) % 8] ^ b[(i+7) % 8] ^ c[i]

    # Return the result back as an integer
    return _B2I(d, True)


def pretty(sbox):
    """ Return a pretty printed SBox. """

    # List of Columns
    p = '\n       '
    for i in range(16):
        p += '%02x' % i + '  '
    p += '\n'

    for i in range(70):
        p += '-'
    p += '\n'

    # Row
    for i in range(16):
        p += '%02x' % i + '  |  '

        # Entries
        for j in range(16):
            p += '%02x' % sbox[16*i+j] + '  '
        p += '\n'

    return p.upper()
