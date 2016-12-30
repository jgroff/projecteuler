import math

def solveProblem006():
    """ Solves Project Euler Problem 006 """
    sumOfSquares = sum([x*x for x in range(1,101,1)])
    squareOfSums = math.pow(sum([x for x in range(1,101,1)]),2)
    print(squareOfSums - sumOfSquares)

if __name__ == "__main__":
    solveProblem006()
