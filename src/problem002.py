def fibonacci():
    """ Generates Fibonacci numbers starting at 0, 1, ... """
    a = 0
    b = 1
    while True:
        yield a
        temp = a
        a = b
        b = temp + b

def solveProblem002():
    """ Solves Project Euler Problem 002 """
    sum = 0
    fib = fibonacci()
    for x in fib:
        if x >= 4000000:
            break
        if (x % 2) == 0:
            sum += x
    print(sum)

if __name__ == "__main__":
    solveProblem002()
