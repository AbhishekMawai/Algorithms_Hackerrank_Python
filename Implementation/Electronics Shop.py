s, n, m = input().strip().split(' ')
s, n, m = [int(s), int(n), int(m)]
keyboards = set([int(keyboards_temp) for keyboards_temp in input().strip().split(' ')])
pendrives = set([int(pendrives_temp) for pendrives_temp in input().strip().split(' ')])
if min(keyboards) + min(pendrives) > s:
    print(-1)
else:
    maxtotal = 0
    for x in keyboards:
        for y in pendrives:
            value = x + y
            if value <= s and value > maxtotal:
                maxtotal = value
    print(maxtotal)
