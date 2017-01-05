def solveProblem017():
    """ Solves Project Euler Problem 016 """
    # This is another problem that was probably a lot harder 10 years ago.
    n = 2**1000
    s = str(n)
    sum = 0
    for x in s:
        sum += int(x)
    print("The sum of the digits of 2^1000 is %d" % (sum,))

if __name__ == "__main__":
    solveProblem016()
