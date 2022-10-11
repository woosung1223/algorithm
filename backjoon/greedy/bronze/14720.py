N = int(input())
lst = list(map(int, input().split(' ')))

flag = 2
result = 0

for element in lst:
    if element == 0 and flag == 2:
        flag = 0
        result += 1
    elif element == 1 and flag == 0:
        flag = 1
        result += 1
    elif element == 2 and flag == 1:
        flag = 2
        result += 1

print(result)