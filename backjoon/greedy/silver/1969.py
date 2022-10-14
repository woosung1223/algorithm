N, M = map(int, input().split(' '))
DNA_list = []

for i in range(N):
    DNA_list.append(input())

result_str = ""
result_distance = 0
temp = ['A', 'C', 'G', 'T']
for i in range(M):
    count = [0,0,0,0] # A - C - G - T 의 개수가 저장됨 (사전순)
    for j in range(N):
        if DNA_list[j][i] == 'A':
            count[0] += 1
        elif DNA_list[j][i] == 'C':
            count[1] += 1
        elif DNA_list[j][i] == 'G':
            count[2] += 1
        else:
            count[3] += 1

    result_str += temp[count.index(max(count))]
    result_distance += N - max(count)

print(result_str)
print(result_distance)