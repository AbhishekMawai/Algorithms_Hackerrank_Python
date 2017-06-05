n = int(input().strip())
B = input().strip()
count = 0
while "010" in B:
    count += 1
    ind = B.find("010")
    BL = list(B)
    BL[ind + 2] = "1"
    B = "".join(BL)
print(count)
