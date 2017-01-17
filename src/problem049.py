from util.primes import getPrimeRange

def solveProblem049():
    """ Solves Project Euler Problem 049 """
    primes = getPrimeRange(1000, 10000)
    for i in range(len(primes)):
        for j in range(i + 1, len(primes)):
            nextVal = primes[j] + (primes[j] - primes[i])
            if nextVal in primes:
                # Ok, this is an arithmetic sequence. See if the 4 digits are
                # permutations.
                a = [s for s in str(primes[i])]
                b = [s for s in str(primes[j])]
                c = [s for s in str(nextVal)]
                a.sort()
                b.sort()
                c.sort()
                if a == b:
                    if b == c:
                        print("Sequence Found, Values: %d, %d, %d" %
                              (primes[i], primes[j], nextVal))


if __name__ == "__main__":
    solveProblem049()
