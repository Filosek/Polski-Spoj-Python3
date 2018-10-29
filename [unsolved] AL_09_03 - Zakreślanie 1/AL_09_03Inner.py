import sys


def collinear(x1, y1, x2, y2, x3, y3):

    a = x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)

    return a


try:

    tests = int(input())

    for t in range(tests):

        is_collinear = True
        points = int(input())

        inputs = list(map(int, input().split()))

        x1 = inputs[0]
        y1 = inputs[1]

        if points > 1:

            inputs = list(map(int, input().split()))

            x2 = inputs[0]
            y2 = inputs[1]

            if points > 2:

                for p in range(0, points-2):

                    inputs = list(map(int, input().split()))

                    x3 = inputs[0]
                    y3 = inputs[1]

                    if collinear(x1, y1, x2, y2, x3, y3) != 0:
                        is_collinear = False

        if is_collinear:
            print("TAK")
        else:
            print("NIE")

except:
    sys.exit(0)
