N, K = map(int, input().split(' '))
# K 원을 만드는데 필요한 동전 개수의 최솟값
money_list = []
for i in range(N):
    temp = int(input())
    money_list.append(temp)

result = 0
# 큰 단위부터 나눌 수 있음 나누고, 아님 내려가고.. 반복
money_list.sort(reverse=True)
for element in money_list:
    result += K // element
    K %= element

print(result)