from math import factorial

def solveProblem024():
    """ Solves Project Euler Problem 024 """
    # Find the millionth lexicographical permutation of the digits 0 through 9.
    # There are 10! permutations. There are 10!/10 that start with 0, or 1,
    # etc.
    x = 1000000
    prePos = []
    fact = 9
    vals = [i for i in range(10)]
    # There is only one way to order everything. Figure out the order of
    # the numbers for the millionth entry.
    while x > 0:
        sub = factorial(fact)
        i = 0
        while x > sub:
            i += 1
            x -= sub
        prePos.append(vals[i])
        del vals[i]
        fact -= 1
        if fact < 0:
            break

    s = "".join(str(n) for n in prePos)
    print("The millionth lex perm is %s" % (s,))
        
if __name__ == "__main__":
    solveProblem024()
