N = int(input())
save_N = N
result = 0
# 5, 2
# 0 또는 1의 값이 남음
# 0의 경우는 종료, 1의 경우는 5를 하나 더해주고 2로 나누어야 함
# 즉, 5원짜리 동전은 하나 빼고 2원짜리 동전 3개로 넣어야 함
# result = result + 2
# 만약 거슬러 줄 수 없다면 -1
while N // 5 != 0:
    result += N // 5
    N %= 5


while N // 2 != 0:
    result += N // 2
    N %= 2

if N + 5 > save_N and N != 0:
    result = -1
elif N != 0:
    result += 2

print(result)
