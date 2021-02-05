N = int(input())
# 배열에 삽입
arr = list(map(int,input().split()))
# N번 1을 삽입한 list 생성
dp = [1] * N

for i in range(N):
    for j in range(i):
        # arr[i]의 기준에서 arr[j]보다 클 경우 쌓아놓은 dp[j]의 위치보다 +1일 것이다
        # 왜냐하면 해당 위치 다음에 올 것이기 떄문에
        if arr[i] > arr[j]:
            dp[i] = max(dp[i],dp[j]+1)

print(max(dp))

# 뒤에서부터 반복문을 돌릴 것
order = max(dp)
result = []

for i in range(N-1, -1, -1):
    if order == dp[i]:
        result.append(arr[i])
        order -= 1

result.reverse()

for i in result:
    print(i,end=" ")

