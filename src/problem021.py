from util.factors import getProperDivisors
import time

def solveProblem021():
    """ Solves Project Euler Problem 021 """
    total = 0
    for i in range(2, 10000):
        divs = getProperDivisors(i)
        s = sum(divs)
        # Skip stuff greater than, we'll get to it later if it's less than max.
        if s > i:
            continue
        if s == i:
            continue
        t = sum(getProperDivisors(s))
        if t == i:
            total = total + i + s
    print("The Sum is: %d" % (total,))

if __name__ == "__main__":
    solveProblem021()
