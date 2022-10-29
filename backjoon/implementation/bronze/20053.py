testCase = int(input())
result_list = []
for _ in range(testCase):
    N = int(input())
    line = list(map(int, input().split(' ')))
    line.sort()
    result_list.append((line[0], line[-1]))

for element in result_list:
    print(element[0], element[1])