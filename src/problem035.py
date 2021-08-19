from util.primes import generateMorePrimes, getPrimeRange

def getRotations(num):
    """ Returns all the rotations of a number """
    s = str(num)
    rots = []
    for i in range(len(s)):
        se = s[i:] + s[:i]
        rots.append(int(se))
    return rots



def solveProblem035():
    """ Solves Project Euler Problem 035 """
    generateMorePrimes(1000000)
    primes = getPrimeRange(11, 999999)
    # No primes (except trivial) end in 2, 4, 6, 8, 0 and 5.
    # So any primes that contain those numbers are out.
    goodPrimes = []
    for p in primes:
        s = str(p)
        if ('2' in s) or ('4' in s) or ('6' in s) or \
            ('8' in s) or ('0' in s) or ('5' in s):
            continue
        goodPrimes.append(p)
    # 1, 3, 7, 9 only
    # Start with 2, 3, 5, 7
    primeList = [2, 3, 5, 7]
    totalPrimes = 4
    for p in goodPrimes:
        rots = getRotations(p)
        good = True
        for r in rots:
            if r not in goodPrimes:
                good = False
        if good:
            totalPrimes = totalPrimes + 1
            primeList.append(p)
    print(primeList)
    print("Total Primes: %d" % totalPrimes)
        
    
 
if __name__ == "__main__":
    solveProblem035()
