# 8진수를 입력받아 2진수로 변환하는 프로그램

num = input()

if int(num) == 0:
    print(0)

else:
    for i in range(len(num)):
        tmp = int(num[i])
        # 첫 수에 앞에 0이 안들어갈 수 있도록 조건설정
        if i == 0 and tmp < 4:    
            if tmp == 1:
                print(1,end="")
            else:
                print(int(tmp % 4 == 2 or tmp % 8 == 3 or tmp % 8 == 7),end="")
                print(int(tmp % 2 == 1),end="")
            continue
        print(int(tmp/4),end="")
        print(int(tmp % 4 == 2 or tmp % 8 == 3 or tmp % 8 == 7),end="")
        print(int(tmp % 2 == 1),end="")
    