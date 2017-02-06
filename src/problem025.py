def getFib():
    """ Gets numbers of the fibonacci sequence, beginning with 1, 1, 2, 3, ...
    """
    yield 1
    yield 1
    f1 = 1
    f2 = 1
    while True:
        f2, f1 = f2 + f1, f2
        yield f2

def solveProblem025():
    """ Solves Project Euler Problem 025 """
    bigNum = int("1" + "0" * 999)
    i = 0
    fib = getFib()
    while True:
        i += 1
        f = next(fib)
        if f >= bigNum:
            break
        if (i % 100000) == 0:
            print("On index %d" % (i, ))
    print("The index of the first term to contain 1000 digits is %d" % (i,))

        
if __name__ == "__main__":
    solveProblem025()
