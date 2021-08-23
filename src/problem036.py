def isPalindrome(s):
    return s == s[::-1]

def solveProblem036():
    """ Solves Project Euler Problem 036 """
    sum = 0
    vals = []
    for n in range(0, 1000000):
        if (isPalindrome(str(n))):
            if (isPalindrome(bin(n)[2:])):
                sum = sum + n
                vals.append(n)
    print("Numbers: %s" % vals)
    print("Sum: %d" % sum)
        
    
 
if __name__ == "__main__":
    solveProblem036()
