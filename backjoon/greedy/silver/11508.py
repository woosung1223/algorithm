N = int(input())
cost = []

for i in range(N):
    cost.append(int(input()))

# 최소비용으로 유제품을 구입하자 -> 정렬 후 3 개씩 묶으면 차가 최소가 됨!
# 즉, (1, 2, 10) 이라면 12원을 내야 하지만, (1, 2, 3) 이라면 5원만 내면 됨
# 따라서 정렬 후 묶음
# 그리고 나머지 값 처리도 해야 함

cost.sort(reverse=True)
result = 0

for i in range(N - N % 3):
    if i % 3 != 2:
        result += cost[i]

for i in range(N - N%3, N):
    result += cost[i]
print(result)
