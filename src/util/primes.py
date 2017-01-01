from math import ceil, sqrt

# Note that the list of primes is not pre-generated. Whenever a new program
# calls a function from this, the primes must be generated initially. This
# module automatically generates up to MAX_PRIME_VAL
MAX_PRIME_VAL = 3000000
_primes = [2, 3, 5]

def __generatePrimes():
    """ Generates primes using the Sieve of Atkin """
    # NOTE: Performance of the implementation if ths sieve can still be
    # improved.
    global _primes
    isPrime = [False] * (MAX_PRIME_VAL + 1)
    for x in range(1, int(ceil(sqrt(MAX_PRIME_VAL + 1)))):
        for y in range(1, int(ceil(sqrt(MAX_PRIME_VAL + 1)))):
            n = (4 * x * x) + (y * y)
            if n < MAX_PRIME_VAL + 1:
                if (n % 60) in [1, 13, 17, 29, 37, 41, 49, 53]:
                    isPrime[n] = not isPrime[n]
            n = (3 * x * x) + (y * y)
            if n < MAX_PRIME_VAL + 1:
                if (n % 60) in [7, 19, 31,43]:
                    isPrime[n] = not isPrime[n]
            if (x > y):
                n = (3 * x * x) - (y * y)
                if n < MAX_PRIME_VAL + 1:
                    if (n % 60) in [11, 23, 47, 59]:
                        isPrime[n] = not isPrime[n]
    for n in range(5, int(ceil(sqrt(MAX_PRIME_VAL + 1)))):
        if isPrime[n]:
            for k in range(n * n, MAX_PRIME_VAL + 1, n * n):
                isPrime[k] = False
    for n in range(6, MAX_PRIME_VAL + 1):
        if isPrime[n]:
            _primes.append(n)

def getNthPrime(n):
    """ Gets the Nth prime, starting at 2. (so the 2nd prime is 3, and so on).
    Will only get primes that have been generated, up to MAX_PRIME_VAL.
    """
    global _primes
    if len(_primes) >= n:
        return _primes[n-1]
    else:
        raise ValueError("Module does not have this prime generated")

def getPrimes():
    """ Generated that yields primes in order. The first prime it yields is
    2, the second 3, and so on. Will only yield primes that are below
    MAX_PRIME_VAL in this module. """
    global _primes
    index = 0
    while True:
        if len(_primes) > index:
            yield _primes[index]
            index += 1
        else:
            raise StopIteration()


# When the module is loaded, generate the list of primes
__generatePrimes()
print("Generated %d primes" % (len(_primes),))
print("Highest Prime Generated: %d" % (_primes[-1]))
