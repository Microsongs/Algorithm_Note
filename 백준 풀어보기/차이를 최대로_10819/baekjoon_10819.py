def next_permutation(data, N):
    if N == 1:
        return -1

    for i in range(N-1, 0, -1):
        if data[i] > data[i-1]:
            break
    
    if i == 1 and data[0] > data[1]:
        return -1

    for j in range(N-1,-1,-1):
        if data[j] > data[j-1]:
            break

    data[j], data[i-1] = data[i-1], data[j]
    data = data[:i]+sorted(data[i:])
    return data


num = int(input())
data = list(map(int,input().split()))
data = sorted(data)
max_len = 0

while True:
    data = next_permutation(data, num)
    if data == -1:
        break
    length = 0
    for i in range(num-1):
        length += abs(data[i] - data[i+1])
    max_len = max(max_len, length)

print(max_len)