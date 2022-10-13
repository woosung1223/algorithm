# 서로 다른 N 개의 자연수의 합이 S
# S 가 주어지고 N의 최댓값 ?
S = int(input())

# 최댓값 -> 최대한 많은 서로 다른 수를 더해서 S 를 조합해라
# 1부터 시작해서 점차 값을 올려나가는 로직은 간단
# 예를 들어서 17이라는 값이 주어졌다고 해보자
# 1 + 2 + 3 + 4 + 5 = 15
# 6을 더할 순 없다. 17까지 남은 값은 2.
# 그러면 마지막 값에서 남은 값만큼 더해서 해주면 됨
# 1 + 2 + 3 + 4 + (5+2) = 17
# 결국 그냥 1부터 더하다가 S를 언제 넘기는지만 count하면 답.

stack = 0
count = 0
for i in range(1, S):
    stack += i
    if stack > S:
        break
    count += 1

if S == 1:
    count = 1 # 1인 경우 예외처리
print(count)