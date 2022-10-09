N = int(input())
conf_list = []

for i in range(N):
    x, y = map(int, input().split(' '))
    conf_list.append((x, y))

conf_list.sort(key = lambda x : (x[1], x[0]))
# x 값 기준 정렬
