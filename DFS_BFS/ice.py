# Page 150 음료수 얼려먹기

N, M = list(map(int,input().split(' ')))
matrix = []

for i in range(N):
    temporary_list = []
    line = list(map(int, list(input())))
    matrix.append(line)

# 입력부 종료

# 0을 찾아서 BFS 혹은 DFS 로 모두 2로 바꿔버림.
# 종료되면 count += 1

def my_dfs(graph, i, j):
    if  0 <= i and i < N and 0 <= j and j < M and graph[i][j] == 0:
        graph[i][j] = 2
        my_dfs(graph, i+1, j)
        my_dfs(graph, i-1, j)
        my_dfs(graph, i, j+1)
        my_dfs(graph, i, j-1)
a = []

count = 0

for i in range(len(matrix)):
    while 0 in matrix[i]:
        j = matrix[i].index(0)
        count += 1
        my_dfs(matrix, i, j)


print(count)

# 로직
# 0의 묶음 개수를 알아내는 것이 목표
# 그러면 0을 하나 찾고, 그 0에서부터 DFS로 모든 0을 찾으면 된다
# 모든 0을 찾으면 모두 2로 바꿔주고, count를 1개 늘린다
# 그래프에서 0이 없어질때까지 반복하면 count가 정답

