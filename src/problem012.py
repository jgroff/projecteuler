from math import sqrt, ceil

def findFactors(n):
    """ Finds the factors of the given positive integer, n.
        Returns array of factors. """
    factors = []
    for i in range(1, int(ceil(sqrt(n)))):
        if (n % i) == 0:
            factors.append(i)
            opp = n / i;
            if (opp != i):
                factors.append(n / i)
                
    return factors

def solveProblem012():
    """ Solves Project Euler Problem 012 """
    n = 0
    t = 0
    while True:
        n += 1
        t += n
        factors = findFactors(t)
        if len(factors) > 500:
            break
    print("Triangle Number %d has %d factors" % (t, len(factors)))


if __name__ == "__main__":
    solveProblem012()
