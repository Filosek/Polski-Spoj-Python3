import sys

try:
    tests = int(input())
    for t in range(tests):
        box_info = list(map(int, input().split()))
        items = list(map(int, input().split()))
        items.sort(reverse=True)
        boxes = 0
        weight = 0
        while len(items) != 0:
            for i in items:
                if weight+i <= box_info[1]:
                    weight += i
                    items.remove(i)
            boxes += 1
            weight = 0
        print(boxes)
                    

except:
    sys.exit(0)