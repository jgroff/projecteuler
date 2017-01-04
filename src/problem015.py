from math import factorial

def solveProblem015():
    """ Solves Project Euler Problem 015 """
    # The lattice problem reduces to a simple combination problem. For an n x n
    # grid, there are n rights and n downs, so out of 2n, pick k=n
    # C(n,k) = n! / (n-k)!k!
    # n = grid size * 2
    # k = grid size
    gridSize = 20
    n = gridSize * 2
    k = gridSize
    ways = factorial(n)/(factorial(n - k) * factorial(k))
    print("%d possible routes" % (ways,))

if __name__ == "__main__":
    solveProblem015()
