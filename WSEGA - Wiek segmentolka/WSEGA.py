import sys

try:
    t = int(input())
    for i in range(t):
        n = list(map(int, input().split()))
        seg = n[0] - 1
        n.pop(0)
        legs = sum(n)
        print(seg + legs)
except:
    sys.exit(0)
