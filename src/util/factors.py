from itertools import *
from util.primes import getPrimeFactors

def getProperDivisors(n):
    """ Returns a list of the proper divisors of n. """
    f = getPrimeFactors(n)
    # Copied from powerset in the itertools documentation.
    allSets = chain.from_iterable(combinations(f, r) for r in range(len(f)+1))
    divs = [1]
    for s in allSets:
        m = 1
        for i in s:
            m *= i
        divs.append(m)
    # Make sure there's no duplicates (because there will be, sorta a brain
    # dead implementation)
    divs = list(set(divs))
    # remove n itself.
    try:
        divs.remove(n)
    except ValueError:
        pass
    return divs
