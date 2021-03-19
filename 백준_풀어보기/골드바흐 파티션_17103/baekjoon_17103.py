# isPrime
def isPrime(n):
    for i in range(2, (n/2)+1):
        if n%i == 0:
            return False
    return True

#에라토스테네스의 체
def eratos(max):
    a = [False, False] + [True] * (max-1)
    for i in range(2, max+1):
        if a[i]:
            primes.append(i)
            for j in range(2*i, max+1, i):
                a[j] = False
    return a

# 골드바흐 파티션을 구하는 함수
def goldbach(arr, primes):
    # arr의 개수만큼 반복
    for num in arr:
        result = 0
        # num/2+1만큼만 반복해주면 된다 5,7과 7,5는 동일하므로
        for i in range((num//2)+1):
            if primes[i] and primes[num-i]:
                result += 1
        print(result) 

n = int(input())
max = 0
primes = []
arr = []
for i in range(n):
    k = int(input())
    if max < k:
        max = k
    arr.append(k)

primes = eratos(max)
goldbach(arr, primes)
