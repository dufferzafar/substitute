""" Bijectivity of a an SBox. """


def is_bijective(sbox):

    missing = []
    for i in range(len(sbox)):
        if i not in sbox:
            missing.append(hex(i))

    if missing:
        return False, missing
    else:
        return True
