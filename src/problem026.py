def calculateRepeatingDecimal(n, d):
    """ Given a rational fraction with numerator n and denominator d,
    determines the non-repeating and repeating portions of the number.
    Returns two arrays - one with the non-repeating digits, one with
    the repeating digits """
    # Remainders
    remainders = []
    digits = []
    while True:
        q = n // d
        r = n % d
        n = r * 10
        digits.append(q)
        if r == 0:
            # non-repeating decimal case
            return (digits, [])
        if r in remainders:
            break
        remainders.append(r)
    # If we get here, it's a repeating decimal
    i = remainders.index(r)
    return (digits[0 : i + 1], digits[i + 1 : ])

def solveProblem026():
    """ Solves Project Euler Problem 026 """
    biggestDivisor = 0
    biggestCycle = 0
    for i in range(1, 1000):
        (r, n) = calculateRepeatingDecimal(1, i)
        if len(n) > biggestCycle:
            biggestDivisor = i
            biggestCycle = len(n)
    print("Integer %d has longest cycle of length %d" % 
          (biggestDivisor, biggestCycle))
    
if __name__ == "__main__":
    solveProblem026()
