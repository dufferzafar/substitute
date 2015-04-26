# Import all functions here
from .diffprob import differential_probability
from .nonlin import non_linearity
from .degree import algebraic_degree
from .bijective import is_bijective


def values(sbox):
    """ Calculate standard parameters. """
    nl = non_linearity(sbox)
    dp = differential_probability(sbox)
    bj = str(is_bijective(sbox))

    return (nl, dp, bj)


def report(sbox):
    """ Create a report based on all calculated parameters. """

    out = """
Analysis
========

Non Linearity: %d
Differential Probability: %d
Is Bijective? %s
    """

    print(out % values(sbox))
