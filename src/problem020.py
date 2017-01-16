import math

def solveProblem020():
    """ Solves Project Euler Problem 020 """
    # Fairly easy in python...
    s = str(math.factorial(100))
    sum = 0
    for n in s:
        sum += int(n)
    print("Answer is %d" % (sum,))

if __name__ == "__main__":
    solveProblem020()
