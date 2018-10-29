import sys

try:
    original = list(map(str, input().split()))
    krzysztof = list(map(str, input().split()))
    for o in original[:]:
        if len(krzysztof) == 0:
            break
        if krzysztof[0] == o:
            krzysztof.pop(0)
            original.remove(o)

    print(len(original))
    for o in sorted(original):
        print(o)

except:
    sys.exit(0)