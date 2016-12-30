def calcPrimes(n):
    """ Calculate Prime Factors of an Integer """
    if type(n) is not int:
        raise ArgumentException("Requires argument of type int")
    factors = []
    d = 2
    while d * d <= n:
        while (n % d) == 0:
            factors.append(d)
            n /= d;
        d += 1
    if n > 1:
        factors.append(int(n))
    return factors

def solveProblem003():
    """ Solves Project Euler Problem 003 """
    primes = calcPrimes(600851475143)
    print(max(primes))

if __name__ == "__main__":
    solveProblem003()
