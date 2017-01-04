def generateCollatzSeq(n):
    """ Generates the Collatz Sequence for the given number n """
    seq = []
    while True:
        seq.append(n)
        if (n == 1):
            break
        if (n % 2) == 0:
            n = n / 2
        else:
            n = (3 * n) + 1
    return seq

def solveProblem014():
    """ Solves Project Euler Problem 014 """
    longestStart = 0
    longestNumInChain = 0
    for i in range(1,1000000):
        n = generateCollatzSeq(i)
        if len(n) > longestNumInChain:
            longestStart  = i
            longestNumInChain = len(n)
    print("Number %s has the longest chain with %s entries" % \
          (longestStart, longestNumInChain))

if __name__ == "__main__":
    solveProblem014()
