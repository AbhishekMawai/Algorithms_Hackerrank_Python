def is_leap(year):
    leap = False
    if year % 400 == 0:
            leap = True
    elif year % 4 == 0:
        if year % 100 == 0:
            leap = False
        else:
            leap = True
    return leap


def solve(year):
    if year >= 1700 and year <= 1917:
        if year % 4 == 0:
            return "12.09.{}".format(year)
        else:
            return "13.09.{}".format(year)
    elif year >= 1919:
        if is_leap(year):
            return "12.09.{}".format(year)
        else:
            return "13.09.{}".format(year)
    else:
        return "26.09.1918"


year = int(input().strip())
result = solve(year)
print(result)
