from util.primes import generateMorePrimes, getPrimeRange
from util.factors import getProperDivisors

def solveProblem095():
    """ Solves Project Euler Problem 095 """
    MAX_NUMBER = 1000000
    # Need primes up to MAX_NUMBER
    generateMorePrimes(MAX_NUMBER)
    nums = [n for n in range(3, MAX_NUMBER + 1)]
    primes = set(getPrimeRange(1, MAX_NUMBER))
    # Remove all primes from the list to shorten the list.
    nums = [n for n in nums if n not in primes]
    # Create a list of all the sums of the proper divisors - we do this once.
    sumDivs = [sum(getProperDivisors(n)) for n in nums]
    # Shove the lists into a dictionary.
    numsDivsums = dict(zip(nums, sumDivs))
    # Iterate through the dictionary to find the chains.
    smallestLongestChainVal = MAX_NUMBER
    longestChainLen = 0
    for startNum in numsDivsums:
        # Start the chain.
        chain = [startNum]
        nextNum = numsDivsums[startNum]
        while True:
            # If the next value in the chain is greater than our max, bad
            # chain.
            if nextNum > MAX_NUMBER:
                break
            # If the next value is 1, stop, bad chain.
            if nextNum == 1:
                break
            # Get the next number - if it's not in the dictionary, stop,
            # bad chain (shouldn't catch, MAX_NUMBER check should handle this)
            try:
                nextNum = numsDivsums[nextNum]
            except KeyError:
                break
            # If the next number is already in the chain, we've completed
            # a chain. Slice it at the repeating point and perform calcs.
            if nextNum in chain:
                i = chain.index(nextNum)
                chain = chain[i:]
                if len(chain) > longestChainLen:
                    longestChainLen = len(chain)
                    smallestLongestChainVal = min(chain)
                break
            # If no other conditions are true, we have the next number
            # in the chain. Append and continue.
            chain.append(nextNum)

    print("Length of longest chain: %s   Smallest value in chain: %d" %
            (longestChainLen, smallestLongestChainVal))
            
if __name__ == "__main__":
    solveProblem095()
