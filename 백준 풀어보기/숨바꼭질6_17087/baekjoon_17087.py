# 각각의 거리를 distance에 저장한다
def dist(distance, arr, s):
    for i in arr:
        distance.append(abs(s - i))

def result(distance):
    # distance가 1일 경우 해당값 리턴
    result = 0
    if len(distance) == 1:
        result = distance[0]
    else:
        result = gcd(distance[0],distance[1])
        for i in range(1,len(distance)-1):
            result = gcd(result,distance[i+1])
    return result

# 최대공약수 
def gcd(a, b):
    while b != 0:
        a = a % b
        a,b = b,a
    return a

# n : 입력받을 숫자 s : 시작점
temp = map(int, input().split())
temp = list(temp)
n = temp[0]
s = temp[1]

# n만큼 입력
arr = map(int,input().split())

arr = list(arr)
distance = []

dist(distance, arr, s)
print(result(distance))
