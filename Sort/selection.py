#selection
def selection(arr):
    # 0부터 n-1까지 반복
    for i in range(0, len(arr)-1):
        #i값을 잡고 min으로 둔 다음 min값을 계속 찾는다
        min = i
        # i+1부터 n까지 반복, 가장 작은 값을 찾아 min에 저장
        for j in range(i, len(arr)):
            if arr[min] > arr[j]:
                min = j
        # i번째 인덱스와 제일 작은 값을 swap
        arr[min], arr[i] = arr[i], arr[min]

# main
data = [int(x) for x in input("여러개 숫자 입력 : ").strip().split()]

print("원본 데이터 : ",data)
selection(data)
print("정렬 후 데이터 : ",data)