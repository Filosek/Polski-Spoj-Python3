import sys

try:
    tests = int(input())
    for t in range(tests):
        entry = input()
        ans = int(entry[0])
        for i in range(len(entry)):
            if entry[i] == "+":
                ans += int(entry[i+1])
            elif entry[i] == "-":
                ans -= int(entry[i+1])
        print(ans)

except:
    sys.exit(0)
