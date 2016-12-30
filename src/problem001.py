def solveProblem001():
    """ Solves Project Euler Problem 001 """
    sum = 0
    for i in range(1000):
        if ((i % 3) == 0) or ((i % 5) == 0):
            sum += i
    print("%s" % (sum,))

if __name__ == "__main__":
    solveProblem001()
