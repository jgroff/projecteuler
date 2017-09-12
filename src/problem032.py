from util.factors import getProperDivisors

def solveProblem032():
    """ Solves Project Euler Problem 032 """
    # There must be a total of 9 digits in the mutiplicand, multiplier,
    # and product combined. Therefore the product must be a 4 digit number.
    # Reasoning:
    # To get 10000 or more, that leaves 4 digits for the multiplier and
    # multiplicand. 99*99 and 9*999 (which are invalid anyways) are both
    # less than 10000.
    # To get less than 1000, means leaving 6 digits for the multiplier
    # and multiplicand, and the lowest possible values are 1 * 10000,
    # 10 * 1000, and 100 * 100, which, besides being invalid, are all
    # greater than 4 digits.
    # That leaves 4 digits in the product.
    # And a posibility of 1 and 4 or 2 and 3 digits in the multiplicand/
    # multiplier.
    #
    # For all the values between 1000 and 9999, calculate divisors,
    # make sets of the numbers that make up the value and divisors, and if
    # the list len is 9 and set len is 9, then we have a winner.
    products = []
    for p in range(1000, 10000):
        divs = getProperDivisors(p)
        # divs will include the value 1. divs is not ordered.
        divs.sort()
        divs = divs[1:]
        # If len is odd, then this is just to the left of the middle value,
        midpointl =len(divs) // 2
        if (len(divs) % 2) == 0:
            midpointr = midpointl
        else:
            midpointr = midpointl + 1
        for d1, d2 in zip(divs[:midpointl], reversed(divs[midpointr:])):
            s = str(d1) + str(d2) + str(p)
            if len(s) == 9 and len(set(s)) == 9 and ('0' not in s):
                # Got it!
                #print(s, d1, d2)
                products.append(p)
                #print(divs)
                break
    print("The products that meet the criteria are: %s" % products)
    print("The sum of those products is %s" % sum(products))
        
 
if __name__ == "__main__":
    solveProblem032()
