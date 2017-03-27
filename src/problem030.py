convDict = {
    "0" : 0**5,
    "1" : 1**5,
    "2" : 2**5,
    "3" : 3**5,
    "4" : 4**5,
    "5" : 5**5,
    "6" : 6**5,
    "7" : 7**5,
    "8" : 8**5,
    "9" : 9**5,
}

def solveProblem030():
    """ Solves Project Euler Problem 030 """
    # The limit that we'll search up to is 354294 which is < 999999
    # i.e., we're searching up to 6 digit numbers.
    nums = []
    for n in range(2, 354295):
        s = 0
        numString = str(n)
        for num in numString:
            s += convDict[num]
        if s == n:
            nums.append(n)
    print("The sum of all numbers that can be written as the sum of the")
    print("5th power of their digits is %d" % (sum(nums)))

    
if __name__ == "__main__":
    solveProblem030()
