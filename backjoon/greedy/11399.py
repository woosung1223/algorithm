N = int(input())
time_list = list(map(int, input().split(' ')))

time_list.sort()
result = 0

for i in range(N):
    for j in range(i+1):
        result += time_list[j]


print(result)