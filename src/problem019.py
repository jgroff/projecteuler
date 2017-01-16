_dow_19000101 = 0
_dInM = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def getDayOfWeek(year, month, day):
    """ Gets the day of the week given the year, month and day. Year must
    be between 1900 and 2100.
    Returns 0 through 6, where 0 is Monday, and 6 is Sunday. """
    if year < 1900 or year > 2100:
        raise ValueError("Year must be between 1900 and 2100")
    if month < 1 or month > 12:
        raise ValueError("Month must be between 1 and 12")
    if day < 1 or day > 31:
        raise ValueError("Day must be between 1 and 31")
    # Initialize
    cDay = _dow_19000101
    # Flip to the correct year.
    cYear = 1900
    while year > cYear:
        if (cYear % 400) == 0:
            cDay += 366
        elif (cYear % 100) == 0:
            cDay += 365
        elif (cYear % 4) == 0:
            cDay += 366
        else:
            cDay += 365
        cYear += 1
    # In the correct year. Flip to the correct month.
    cMonth = 1
    while month > cMonth:
        cDay += _dInM[cMonth]
        cMonth += 1
    # Correct for leap year
    isLeap = False
    if (year % 400) == 0:
        isLeap = True
    elif (year % 100) == 0:
        isLeap = False
    elif (year % 4) == 0:
        isLeap = True
    if month >= 3 and isLeap:
        cDay += 1
    # In the correct month. Flip to the correct day
    cDay += day - 1
    # Alrighty, what day of the week is it?
    return cDay % 7


def solveProblem019():
    """ Solves Project Euler Problem 019 """
    firstSundays = 0
    for year in range(1901, 2001, 1):
        for month in range(1, 13, 1):
            if getDayOfWeek(year, month, 1) == 6:
                firstSundays += 1
    print("The number of Sundays on the First of the Month in the 20th Century")
    print("%d" % (firstSundays,))


if __name__ == "__main__":
    solveProblem019()
