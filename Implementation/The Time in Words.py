h = int(input().strip())
m = int(input().strip())
time = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "quarter", "sixteen", "seventeen", "eighteen",
        "nineteen", "twenety", "twenty one", "twenty two", "twenty three", "twenty four", "twenty five", "twenty six", "twenty seven", "twenty eight", "twenty nine", "half"]

if m == 0:
    print("{} o' clock".format(time[h - 1]))
elif m == 15:
    print("{} past {}".format(time[m - 1], time[h - 1]))
elif m == 30:
    print("{} past {}".format(time[m - 1], time[h - 1]))
elif m > 0 and m <= 9:
    print("{} minute past {}".format(time[m - 1], time[h - 1]))
elif m >= 10 and m < 30:
    print("{} minutes past {}".format(time[m - 1], time[h - 1]))
elif m == 60:
    print("{} o' clock".format(time[h]))
elif m == 45:
    u = 60 - m
    if h == 12:
        h = 0
    print("{} to {}".format(time[u - 1], time[h]))
elif m > 30 and m < 60:
    u = 60 - m
    if h == 12:
        h = 0
    print("{} minutes to {}".format(time[u - 1], time[h]))
