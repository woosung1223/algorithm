# 설탕 배달
# 3, 5의 최소개수 조합으로 N 만들기
# 만들 수 없다면 -1

N = int(input())
save_N = N
result = 0

result += N // 5
N = N % 5
# 0 ~ 4 의 값이 남음
count = 0
while N % 3 != 0:
    if N + 5 <= save_N:
        N += 5
    result -= 1
    count += 1

    if count == 2:
        break

if N % 3 == 0:
    result += N // 3
else:
    result = -1

print(result)

