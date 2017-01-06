_numWordDict = {
    1 : "one",
    2 : "two",
    3 : "three",
    4 : "four",
    5 : "five",
    6 : "six",
    7 : "seven",
    8 : "eight",
    9 : "nine",
    10 : "ten",
    11 : "eleven",
    12 : "twelve",
    13 : "thirteen",
    14 : "fourteen",
    15 : "fifteen",
    16 : "sixteen",
    17 : "seventeen",
    18 : "eighteen",
    19 : "nineteen",
    20 : "twenty",
    30 : "thirty",
    40 : "forty",
    50 : "fifty",
    60 : "sixty",
    70 : "seventy",
    80 : "eighty",
    90 : "ninety",
    100 : "hundred",
    1000 : "thousand"
}

def solveProblem017():
    """ Solves Project Euler Problem 017 """
    lens = {k:len(v) for (k,v) in _numWordDict.items()}
    # Could just go number by number, but instead lets be a bit more logical
    # about the algorithm.
    # Numbers 1 - 99
    len1to19 = 0
    for i in range(1,20):
        len1to19 += lens[i]
    len20to99 = 0
    # 10 of each tens unit
    for i in range(20,100,10):
        len20to99 += lens[i] * 10
    # Then 8 of each ones unit
    for i in range(1,10):
        len20to99 += lens[i] * 8
    len1to99 = len1to19 + len20to99
    # Lets calculate all 1000 now.
    len1to1000 = 0
    # Alright, now between 1 and 1000 inclusive, 1 through 99 are used 10 times
    len1to1000 += len1to99 * 10
    # "hundred" is used 900 times
    len1to1000 += lens[100] * 900
    # "and" after hundred is used 900 - 9 times
    len1to1000 += 3 * (900 - 9)
    # Now the hundred qualifiers "one" hundred "two" hundred etc. are each used
    # 100 times
    for i in range(1,10):
        len1to1000 += lens[i] * 100
    # Finally one thousand
    len1to1000 += lens[1000] + lens[1]
    print("Total letters in words between one and one thousand inclusive: %d" %
          (len1to1000,))

if __name__ == "__main__":
    solveProblem017()
