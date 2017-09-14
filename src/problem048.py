def solveProblem048():
    """ Solves Project Euler Problem 048 """
    # Trivial to brute force with modern hardware.
    sd = 0
    for i in range(1,1000+1):
        sd += i**i
    s = str(sd)
    s = s[-10:]
    print(s)

if __name__ == "__main__":
    solveProblem048()
