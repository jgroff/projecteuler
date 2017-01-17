from util.primes import getPrimeFactors

def solveProblem047():
    """ Solves Project Euler Problem 047 """
    n = 1
    inRow = 0
    while True:
        factors = getPrimeFactors(n)
        if len(set(factors)) == 4:
            inRow += 1
            if inRow == 4:
                break
                pass
        else:
            inRow = 0
        n += 1
    print("The first of the consecutive integers is %d" % ((n - 3,)))

if __name__ == "__main__":
    solveProblem047()
