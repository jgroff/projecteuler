from math import log, ceil

def solveProblem013():
    """ Solves Project Euler Problem 013 """
    # This problem would be much more difficult if it were done in C or
    # another language where integer size is a problem. As it is, it's fairly
    # simple in python.
    f = open("../problemdata/data013.txt", 'r')
    numbers = []
    while True:
        line = f.readline()
        if line == "":
            break
        numbers.append(int(line))
    total = sum(numbers)
    s = str(total)
    print("First 10 digits of the sum are %s" % s[:10])


if __name__ == "__main__":
    solveProblem013()
