def solveProblem005():
    """ Solves Project Euler Problem 005 """
    num = 1
    divisors = [x for x in range(20, 0, -1)]
    found = False
    while True:
        found = True
        if (num % 1000000) == 0:
            print("Up to %dM" % (num/1000000,))
        for d in divisors:
            if (num % d) != 0:
                num += 1
                found = False
                break
        if found:
            break
    print(num)

if __name__ == "__main__":
    solveProblem005()
