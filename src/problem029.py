def solveProblem029():
    """ Solves Project Euler Problem 029 """
    values = []
    for a in range (2, 101):
        for b in range(2, 101):
            values.append(a**b)
    values = list(set(values))
    print("The number of distinct terms is: %d" % len(values))

    
if __name__ == "__main__":
    solveProblem029()
