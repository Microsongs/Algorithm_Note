num = int(input())

if not num:
    print("0")
else:
    res = ''
    while num:
        if num%(-2):
            res = "1" + res
            num = num // -2 + 1
        else:
            res = "0" + res
            num //= -2
    print(res)