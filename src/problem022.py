def solveProblem022():
    """ Solves Project Euler Problem 022 """
    f = open("../problemdata/data022.txt")
    raw = f.read()
    f.close()
    raw = raw.replace("\"", "")
    names = raw.split(",")
    names.sort()
    sum = 0
    index = 1
    for name in names:
        subsum = 0
        for s in name.upper():
            subsum += ord(s) - 0x40
        sum += subsum * index
        index += 1

    print("The total sum is %d" % (sum,))

if __name__ == "__main__":
    solveProblem022()
