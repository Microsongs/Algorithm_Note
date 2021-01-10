# 최대공약수 공식 : 유클리드 호제법
def GCD(a, b):
    if a<b:
        a,b = b,a
    while b!=0:
        a,b = b,a%b
    return a

# 1. 반복할 값 입력
cycle = int(input())

# 2. cycle만큼 숫자를 입력받는다
cycle_arr = []
for i in range(cycle):
    cycle_arr.append([int(x) for x in input("").strip().split()])

# 3. 입력받은 숫자로 최대공약수를 구해 합을 출력
#print(cycle_arr)

for cycle in cycle_arr:
    sum = 0
    my_cycle = cycle[0]-1
    for i in range(my_cycle):
        for j in range(my_cycle-i):
            sum += GCD(cycle[i+1],cycle[j+i+2])
    print(sum)