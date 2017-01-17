from math import ceil, sqrt

# Note that the list of primes is not pre-generated. Whenever a new program
# calls a function from this, the primes must be generated initially. This
# module automatically generates up to MAX_PRIME_VAL
MAX_PRIME_VAL = 100000
_primes = [2, 3, 5]
_max_prime = 0

def __generatePrimes(maxPrimeVal=MAX_PRIME_VAL):
    """ Generates primes using the Sieve of Atkin """
    # NOTE: Performance of the implementation if ths sieve can still be
    # improved.
    global _primes
    isPrime = [False] * (maxPrimeVal + 1)
    for x in range(1, int(ceil(sqrt(maxPrimeVal + 1)))):
        for y in range(1, int(ceil(sqrt(maxPrimeVal + 1)))):
            n = (4 * x * x) + (y * y)
            if n < maxPrimeVal + 1:
                if (n % 60) in [1, 13, 17, 29, 37, 41, 49, 53]:
                    isPrime[n] = not isPrime[n]
            n = (3 * x * x) + (y * y)
            if n < maxPrimeVal + 1:
                if (n % 60) in [7, 19, 31,43]:
                    isPrime[n] = not isPrime[n]
            if (x > y):
                n = (3 * x * x) - (y * y)
                if n < maxPrimeVal + 1:
                    if (n % 60) in [11, 23, 47, 59]:
                        isPrime[n] = not isPrime[n]
    for n in range(5, int(ceil(sqrt(maxPrimeVal + 1)))):
        if isPrime[n]:
            for k in range(n * n, maxPrimeVal + 1, n * n):
                isPrime[k] = False
    for n in range(6, maxPrimeVal + 1):
        if isPrime[n]:
            _primes.append(n)
    print("Generated %d primes. Highest Prime Generated: %d" %
          (len(_primes), _primes[-1]))
    global _max_prime
    _max_prime = _primes[-1]

def getNthPrime(n):
    """ Gets the Nth prime, starting at 2. (so the 2nd prime is 3, and so on).
    Will only get primes that have been generated.
    """
    global _primes
    if len(_primes) >= n:
        return _primes[n-1]
    else:
        raise ValueError("Module does not have this prime generated")

def getPrimes():
    """ Generator that yields primes in order. The first prime it yields is
    2, the second 3, and so on. Will only yield primes that have been
    generated. """
    global _primes
    index = 0
    while True:
        if len(_primes) > index:
            yield _primes[index]
            index += 1
        else:
            raise StopIteration()

def getPrimeRange(start, stop):
    """ Gets primes within the specified range. """
    global _primes
    first = next(i for (i, v) in enumerate(_primes) if v >= start)
    last = next(i for (i, v) in enumerate(_primes) if v > stop)
    return _primes[first : last]

def generateMorePrimes(n):
    """ Generates primes up to the given number. Note, by default, module
    loads up to 100,000."""
    __generatePrimes(n)

def getPrimeFactors(n):
    """ Gets the prime factors of the given number. If the number is higher
    than max_prime squared, throws an exception. """
    if n > (_max_prime * _max_prime):
        raise ValueError("Number too large, generate more primes, cur max: %d",
                         (_max_prime,))
    factors = []
    stopPoint = ceil(sqrt(n))
    for i in _primes:
        if i > stopPoint:
            break
        while (n % i) == 0:
            factors.append(i)
            n /= i
    if (n > 1):
        factors.append(int(n))
    return factors


# When the module is loaded, generate the list of primes
__generatePrimes()
