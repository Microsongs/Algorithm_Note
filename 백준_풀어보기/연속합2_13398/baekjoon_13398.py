# 숫자 입력
n = int(input())
# 숫자 배열 입력
arr = list(map(int, input().split()))

# 숫자를 안 뻈을 경우
dp_normal = []
# 숫자를 뺐을 경우
dp_minus = []

# 시작점 = 0
ans = arr[0]

for i in range(n):
    # i번쨰의 값에 arr[i]값을 넣어준다
    dp_normal.append(arr[i])
    dp_minus.append(arr[i])
    #dp_normal[i] = dp_minus[i] = arr[i]
    if(i == 0):
        continue
    # normal에는 전의값+arr값이랑 arr값이랑 비교하여 큰 값 삽입
    dp_normal[i] = max(dp_normal[i-1] + arr[i], arr[i])
    # minus에는 전의 값과 현재값 +1로 비교
    dp_minus[i] = max(dp_normal[i-1], dp_minus[i-1] + arr[i])
    print("normal:",dp_normal[i],"minus:",dp_minus[i])
    ans = max(ans, dp_normal[i], dp_minus[i])

print(ans)