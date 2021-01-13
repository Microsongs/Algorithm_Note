# 음수 -> -2진법 양수 -> 2진법
num = int(input())

stack = []

def binary(num):
    # 양수일 때 -> 연산 그대로
    if num > 0:
        while num != 0:
            stack.append(num%2)
            num = int(num/2)
    #0일때 -> 0 출력
    elif num == 0:
        stack.append(0)
    # 음수일 떄 -> 음수만의 연산
    # 숫자가 -홀수일경우 숫자를 -1 더해주고 연산
    else:
        while num != 0:
            stack.append(abs(num%-2))
            if num%2 == 1:
                num -= 1
            num = int(num/-2)

binary(num)

stack = stack[::-1]
for i in stack:
    print(i,end="")
"""
while stack.count != 0:
    print(stack.pop(),end="")
"""