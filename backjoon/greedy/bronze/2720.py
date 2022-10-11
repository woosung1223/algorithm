lst = [25, 10, 5, 1]
N = int(input())

result_buffer = []
for i in range(N):
    temp = []
    money = int(input())

    for idx in range(len(lst)):
        temp.append(money // lst[idx])
        money %= lst[idx]

    result_buffer.append(temp)


for i in range(len(result_buffer)):
    for j in range(len(lst)):
        print(result_buffer[i][j], end = " ")
    print()

