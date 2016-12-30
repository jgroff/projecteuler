_primes = [2,3]
_lastChecked = 3
def getPrime(n):
    """ Gets the Nth prime, starting at 2. (so the 2nd prime is 3, and so on).
    Calculates the primes and adds them to an array, so if the primes are not
    yet calculated, the first run may take a while.
    """
    global _primes
    global _lastChecked
    if len(_primes) >= n:
        return _primes[n-1]
    while True:
        _lastChecked += 2
        isDivisible = False
        for p in _primes:
            if (_lastChecked % p) == 0:
                isDivisible = True
                break
        if not isDivisible:
            _primes.append(_lastChecked)
            if len(_primes) >= n:
                return _primes[n-1]

def solveProblem007():
    """ Solves Project Euler Problem 007 """
    p = getPrime(10001)
    print(p)

if __name__ == "__main__":
    solveProblem007()
