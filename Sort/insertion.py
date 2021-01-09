#insertion sort
def insertion(arr):
    # 2번째 원소부터 시작
    for i in range(1,len(arr)):
        # key = 변경할 키값 aux = 해당 위치로 삽입 전까지 밀어내는 값
        key = arr[i]
        aux = i-1
        # 숫자를 해당 위치에 삽입하므로 앞은 정렬이 완성, 정렬이 완성된 자리까지 계쏙 반복하여 삽입할 위치를 찾아 삽입한다
        while (aux>=0) and (arr[aux] > key):
            arr[aux+1] = arr[aux]
            aux -= 1
        arr[aux+1] = key

# main
data = [int(x) for x in input("여러개 숫자 입력 : ").strip().split()]

print("원본 데이터 : ",data)
insertion(data)
print("정렬 후 데이터 : ",data)