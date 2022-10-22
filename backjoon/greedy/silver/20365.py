N = int(input())
problems = input()

# R -> 빨간색, B -> 파란색
# 연속된 임의의 문제들을 선택하고 같은 색으로 칠할 수 있다.
# idea -> 처음에 한번 다 R 혹은 B로 칠하고 연속된 R 혹은 B를 다 1로 카운트한다

result = 0
# compress
new_problems = ''
before_i = ''
for i in problems:
    if before_i == i:
        continue
    new_problems += i
    before_i = i


result = min(new_problems.count('B'), new_problems.count('R')) + 1
print(result)