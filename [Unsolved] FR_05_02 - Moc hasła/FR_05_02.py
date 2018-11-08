import sys

try:
    tests = int(input())
    for t in range(tests):
        password = input()
        sign = False
        upper = False
        lower = False
        num = False
        if len(password) < 8:
            continue
        for i in range(len(password)):
            if password[i].isdigit():
                num = True
            elif password[i].islower():
                lower = True
            elif password[i].isupper():
                upper = True
            else:
                sign = True
        if(sign and upper and lower and num):
            print(password)
except:
    sys.exit(0)