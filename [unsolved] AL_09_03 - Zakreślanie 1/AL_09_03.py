import sys


class Point:
    def __init__(self):
        self.x = 0
        self.y = 0


def det(a, b, c):
    d = (a.x*b.y) + (b.x*c.y) + (c.x*a.y) - (c.x*b.y) - (a.x*c.y) - (b.x*a.y)
    return d


try:
    a = Point()
    b = Point()
    c = Point()
    tests = int(input())
    for t in range(tests):
        is_collinear = True
        points = int(input())
        inputs = list(map(int, input().split()))
        a.x = inputs[0]
        a.y = inputs[1]
        if points > 1:
            inputs = list(map(int, input().split()))
            b.x = inputs[0]
            b.y = inputs[1]
        if points > 2:
            for p in range(0, points-2):
                inputs = list(map(int, input().split()))
                c.x = inputs[0]
                c.y = inputs[1]
                if det(a, b, c) != 0:                  #and ((c.x != a.x or c.x != b.x) and (c.y != a.y or c.y != b.y)):
                    is_collinear = False
        if is_collinear:
            print("TAK")
        else:
            print("NIE")

except:
    sys.exit(0)
