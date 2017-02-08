def solveProblem028():
    """ Solves Project Euler Problem 028 """
    diagNums = [1]
    adder = 2
    n = 1
    adderInc = 0
    while n < 1001*1001:
        # Choose n
        n += adder
        diagNums.append(n)
        # Check the adder
        adderInc += 1
        if adderInc == 4:
            adderInc = 0
            adder += 2
    print("The sum of the numbers on the diagonals is %d" % (sum(diagNums)))

    
if __name__ == "__main__":
    solveProblem028()
