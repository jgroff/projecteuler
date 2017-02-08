from util.primes import getPrimeRange

def solveProblem027():
    """ Solves Project Euler Problem 027 """
    primes = getPrimeRange(0, 5000000)
    biggestConseqPrimes = 0
    coefficients = (0, 0)
    # b has to be a prime number or else n = 0 doesn't come out prime
    bRange = getPrimeRange(0, 1000)
    for a in range(-999, 1000, 1):
        print(a)
        for b in bRange:
            n = 0
            numConseqPrimes = 0
            while True:
                if ((n**2) + (a * n) + b) in primes:
                    numConseqPrimes += 1
                    n += 1
                else:
                    break
            if n > biggestConseqPrimes:
                biggestConseqPrimes = n
                coefficients = (a, b)
    print("The coefficients that produce the largest number of consecutive" \
          "primes are a = %d   b = %d" % (coefficients))
    print("The product of the coefficients is %d" % (coefficients[a] * \
            coefficients[b])

if __name__ == "__main__":
    solveProblem027()
