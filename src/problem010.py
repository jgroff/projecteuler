from util.primes import getPrimes, generateMorePrimes

def solveProblem010():
    """ Solves Project Euler Problem 010 """
    generateMorePrimes(2100000)
    sum = 0
    n = 0
    prime = getPrimes()
    while True:
        p = next(prime)
        n += 1
        if p >= 2000000:
            break
        sum += p
    print("Sum of all primes below 2M is: %d" % (sum,))

if __name__ == "__main__":
    solveProblem010()
