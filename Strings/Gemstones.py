n = int(input())
s = set(input())
t = set(input())
int = s.intersection(t)
for i in range(2, n):
    t = set(input())
    int = int.intersection(t)
print(len(int))
