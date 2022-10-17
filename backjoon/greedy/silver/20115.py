N = int(input())
drinks = list(map(int, input().split(' ')))
# idea -> 가장 적은 양의 드링크부터 없애자

drinks.sort()

for i in range(N-1):
    drinks[-1] = drinks[-1] + (drinks[i] / 2)

print(drinks[-1])