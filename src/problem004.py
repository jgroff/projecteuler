def isPalindrome(n):
    """ Determines if the given number is a palindrome. """
    s = str(n)
    r = s[::-1]
    if (s == r):
        return True
    else:
        return False

def solveProblem004():
    """ Solves Project Euler Problem 004 """
    # This is going to be brute forced - I'm sure there's a better algorithm
    # for calculation which is the largest numbers, but I know it's not a
    # simple addition like Pascal's triangle looks like, so...brute force.
    highest = 0
    for i in range(1000):
        for j in range(1000):
            prod = i * j
            if isPalindrome(prod):
                if prod > highest:
                    highest = prod
    print(highest)

if __name__ == "__main__":
    solveProblem004()
