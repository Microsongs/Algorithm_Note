N = int(input())
arr = list(map(int, input().split()))
# 입력받은 N만큼 배열에 삽입
dp = [1]*N

# N까지 반복
for i in range(1,N):
    for j in range(i):
        # 앞 수가 더 클 경우 i와 j의 당므번쨰 수를 하여 넣어준다
        if arr[i] > arr[j]:
            dp[i] = max(dp[i],dp[j]+1)

print(max(dp))
order = max(dp)

lst = []
for i in range(N-1, -1, -1):
    if dp[i] == order:
        lst.append(arr[i])
        order -= 1

lst.reverse()
for i in lst:
    print(i, end = ' ')