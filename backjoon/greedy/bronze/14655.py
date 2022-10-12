N = int(input())
round_1 = list(map(int, input().split(' ')))
round_2 = list(map(int, input().split(' ')))

# 양 끝과, 양 끝에서 한번째는 자유롭게 뒤집을 수 있음
# 즉 항상 최대/최소 가 되도록 할 수 있다는 것이다
# 그러면 연쇄작용으로 모든 동전을 원하는대로 조작할 수 있다는 것
# 그래서 부호만 바꿔주면 됨

result = 0
for element in round_1:
    result += abs(element)

for element in round_2:
    result += abs(element)

print(result)