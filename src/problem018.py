def readNumberTriangle(f):
    """ Reads in a number triangle from the given file """
    data = []
    n = 0
    while True:
        line = f.readline()
        if line == "":
            break
        n += 1
        nums = []
        for i in range(n):
            nums.append(int(line[(i * 3) : (i * 3) + 2]))
        data.append(nums)
    return data

def findHighestNumberTrianglePath(data):
    """ Finds the maximum valued path through the triangle data. Destroys the
    data in the process. """
    for line in range(len(data) - 2, -1, -1):
        for i in range(len(data[line])):
            if data[line + 1][i] > data[line + 1][i + 1]:
                high = data[line + 1][i]
            else:
                high = data[line + 1][i + 1]
            data[line][i] += high
    return data[0][0]

def solveProblem018():
    """ Solves Project Euler Problem 018 """

if __name__ == "__main__":
    solveProblem018()
