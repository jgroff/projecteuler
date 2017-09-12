import copy

def solveProblem031():
    """ Solves Project Euler Problem 031 """
    # Lets just brute force this.
    # 1p, 2p, 5p, 10p, 20p, 50p, 100p, 200p
    # We could make this algorithm much more clever by knowing there's X ways
    # to make 10 cents out of 5,2,1, then make a new metacoin that adds X ways
    # and make 100s etc (or go the opposite direction, there are 1 ways using
    # a 200, x ways using 100 + smaller, etc)
    denoms = [200, 100, 50, 20, 10, 5, 2, 1]
    goal = 200
    ways = []
    stack = []
    dindex = 0
    hitgoal = False
    # Iteration algorithm is keep tacking on the same number. If the same
    # number makes bigger than the goal, reduce number unti less than or
    # equal to. Then reduce that number and continue on.
    # one that number has been reduced to 1, back up to the rightmost
    # non 1, and reduce by one. Continue till we have all 1's.
    while True:
        # If we've incremented dindex past the array, that means we couldn't
        # tack on another number. Set the stack back.
        # We set the stack setback index is either the last value, if there
        # are no ones in the stack, or the value just before a one. That value
        # gets decremented by one denom and we continue
        # This also gets triggered when we get a stack that hits the goal.
        if dindex >= len(denoms) or hitgoal:
            try:
                i = stack.index(1) - 1
            except ValueError: # Not in the list
                i = len(stack) - 1
            val = stack[i]
            # Get the next val - assumption is that this is not 1.
            newval = denoms[denoms.index(val) + 1]
            # Insert it
            stack = stack[:i]
            stack.append(newval)
            # Reset dindex to the same index as newval.
            dindex = denoms.index(newval)
            hitgoal = False
            continue
        # Tack on next number if sum of the stack is less than our goal.
        # Keep trying numbers until we hit a number that makes the sum
        # less than or equal to the goal.
        if sum(stack) + denoms[dindex] <= goal:
            stack.append(denoms[dindex])
        else:
            dindex += 1
        # If we tacked on a next number and we're equal to the goal, add it.
        if sum(stack) == goal:
            #print(stack)
            ways.append(copy.copy(stack))
            #input("Press Enter to continue")
            # Autoadvance to new dindex since we'
            hitgoal = True
            # End condition
            if len(set(stack)) == 1 and len(stack) == goal:
                break
    print("There are %s ways to make %s out of the given denominations of %s" %
            (len(ways), goal, denoms))

    
if __name__ == "__main__":
    solveProblem031()
