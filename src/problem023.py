from util.factors import getProperDivisors

def solveProblem023():
    """ Solves Project Euler Problem 023 """
    # The goal is to find the sum of all positive integers that cannot
    # be written as the sum of two abundant numbers
    
    # Therefore, first, find all positive integers that cannot be written
    # as the sum of two abundant numbers.
    # All integers greater than 28123 can be written as the sum of two
    # abundant numbers.
    # The smallest number that can be written as the sum is 24. (12 + 12)
    # 12 is the smallest abundant number.
    # So:
    # 1. Find all abundant numbers greater than 12 and less than 28123 - 12.
    # 2. Figure out which numbers between 12 and 28123 do not fill criteria.
    # 3. Sum 'em.
    abNums = [12]
    # Find abundant numbers.
    for i in range (13, 28124):
        divs = getProperDivisors(i)
        if sum(divs) > i:
            abNums.append(i)
    # Check against.
    nope = []
    dAbnums = {x:x for x in abNums}
    for i in range(1, 28124-12):
        if (i % 500) == 0:
            print(i)
        isNope = True
        for d in abNums:
            if (i < d):
                break
            if (i - d) in dAbnums:
                isNope = False
                break
        if (isNope):
            nope.append(i)
                

    # Sum
    s = sum(nope)
    print("The sum of values requested is %d" % (s, ))
    
if __name__ == "__main__":
    solveProblem023()
