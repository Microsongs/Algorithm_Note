# bubble sort
def bubble(arr):
    # 0 ~ len-1까지 반복
    for i in range(len(arr)-1, 0, -1):
        # 0~i까지 반복
        for j in range(0, i):
            # 앞 수가 뒷 수보다 클 경우 swap
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

#main
data = [int(x) for x in input("여러개 숫자 입력 : ").strip().split()]

print("원본 데이터 : ",data)
bubble(data)
print("정렬 후 데이터 : ",data)

