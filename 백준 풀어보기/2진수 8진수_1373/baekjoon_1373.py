# 2진수가 주어졌을 때 8진수로 변환하는 문제

data = input()

pos = [1,2,4]

if len(data)%3 == 1:
    data = "00" + data
elif len(data)%3 == 2:
    data = "0" + data

for i in range(0,len(data),3):
    result = int(data[i+2])*1 + int(data[i+1])*2 + int(data[i])*4
    print(result,end="")