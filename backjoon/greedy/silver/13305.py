N = int(input())
distance = list(map(int, input().split(' ')))
liter = list(map(int, input().split(' ')))

# idea -> 현재 위치의 리터 값 보다 작은 리터 값을 만나기 전까지 그 값으로 이동

liter = liter[:-1]

before_min_liter = 1000000001
result_liter = 0

for i in range(N-1):
    if liter[i] < before_min_liter:
        before_min_liter = liter[i]
    result_liter += before_min_liter * distance[i]

print(result_liter)
