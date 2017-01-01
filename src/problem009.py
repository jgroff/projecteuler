def calcGcd(a, b):
    """ Calculates the greatest common divisor between the two integer inputs
    Uses the Euclidean algorithm.
    """
    # Check for equalness, and then make b > a.
    if a == b:
        return a
    if a > b:
        b, a = a, b
    # Loop until there's equality or b < a. If the former, return, if the latter
    # then invert and repeat.
    while True:
        while True:
            b -=a
            if b > a:
                continue
            break
        if b == a:
            return b
        b, a = a, b

def isCoPrime(a, b):
    """ Calculates if two numbers are coprime """
    gcd = calcGcd(a, b)
    if gcd == 1:
        return True
    else:
        return False

def getPythagorianTriple():
    """ A generator that creates and returns primitive Pythagorian Triples. """
    m = 1
    n = 2
    while True:
        # Euclid's formula returns a primitive triple iff m and n are coprime
        # and not both odd.
        bothOdd = (m % 2 == 0) and (n % 2 == 0)
        if (not isCoPrime(m, n)) and (not bothOdd):
            a = (n * n) - (m * m)
            b = 2 * n * m
            c = (n * n) + (m * m)
            yield (a,b,c)
        # Calculate the next m and n
        m += 1
        if m == n:
            n += 1
            m = 1

def solveProblem009():
    """ Solves Project Euler Problem 009 """
    gen = getPythagorianTriple()
    found = False
    while True:
        # Get a triple, check it, and check it's multiples. If no match, get
        # the next triple.
        triple = next(gen)
        a,b,c = triple
        am = a
        bm = b
        cm = c
        while True:
            sum = am + bm + cm
            if sum == 1000:
                found = True
                break
            if sum > 1000:
                break
            am += a
            bm += b
            cm += c
        if found:
            break
    print("Triple is a=%d, b=%d, c=%d" % (am, bm, cm))
    print("Sum is %d" % (sum, ))
    print("Product is %d" % (am * bm * cm, ))


if __name__ == "__main__":
    solveProblem009()
