from util.factors import getProperDivisors

def solveProblem033():
    """ Solves Project Euler Problem 033 """
    # 49/98 = 4/8
    # proper division gives us this, but also if you do a "stupid" division
    # by cancelling the 9s.
    # First find all num/dem pairs that work this way.
    # No numbers with a 0 need be considered.
    # 20/30 -> 2/3 (trival)
    # 15/50 -> 1/0 (undefined)
    # All numbers must be less than 1, so num < dem
    # the following if statements bypass double digit possibilities which is fine
    pairs = []
    for dem in range(11, 100):
        d1 = dem // 10
        d0 = dem % 10
        if (d0 == 0):
            continue
        for num in range (10, dem):
            n1 = num // 10
            n0 = num % 10
            if (d1 == n1) and (d0 > n0):
                if (n0 / d0) == (num / dem):
                    pairs.append((num, dem))
                    continue
            if (d0 == n1) and (d1 > n0):
                if (n0 / d1) == (num / dem):
                    pairs.append((num, dem))
                    continue
            if (d1 == n0) and (d0 > n1):
                if (n1 / d0) == (num / dem):
                    pairs.append((num, dem))
                    continue
            if (d0 == n0) and (d1 > n1):
                if (n1 / d1) == (num / dem):
                    pairs.append((num, dem))
                    continue
    print("All num/dem pairs:")
    print(pairs)
    num = 1
    dem = 1
    for pair in pairs:
        num = num * pair[0]
        dem = dem * pair[1]
    divs = getProperDivisors(dem)
    divs.sort()
    divs.reverse()
    for div in divs:
        if (num / div) == (num // div):
            print ("Value is %d" % (dem / div))
            break
        
 
if __name__ == "__main__":
    solveProblem033()
