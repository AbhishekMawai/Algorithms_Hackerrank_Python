q = int(input().strip())
for a0 in range(q):
    x, y, z = input().strip().split(' ')
    x, y, z = [int(x), int(y), int(z)]
    if abs(z - x) == abs(z - y):
        print("Mouse C")
    elif abs(z - y) > abs(z - x):
        print("Cat A")
    else:
        print("Cat B")
