import math

def solveProblem034():
    """ Solves Project Euler Problem 034 """
    # Upper limit of 2540160. This is because 9!*7 equals
    # that. It's a dumb upper limit but that's ok.
    # Lower limit of 3. 2 and 1 are not included as per
    # the problem.
    totalsum = 0
    for val in range(3, 2540160+1):
        factsum = 0
        i = val
        while i > 0:
            m = i % 10
            factsum = factsum + math.factorial(m)
            i = i // 10
        if factsum == val:
            print("Found an equal: %d" % factsum)
            totalsum = totalsum + factsum
    print("Total Sum: %d" % totalsum)   

 
if __name__ == "__main__":
    solveProblem034()
