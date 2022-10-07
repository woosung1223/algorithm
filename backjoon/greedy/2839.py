# 설탕 배달
# 3, 5의 최소개수 조합으로 N 만들기
# 만들 수 없다면 -1

N = int(input())
save_N = N
result = 0

result += N // 5
N = N % 5

result += N // 3
N = N % 3

# 만약 나머지가 남았는데, 5를 다시 더해서 3으로 만들 수 있는지 테스트하려면
# 3과 5의 공배수인 15 전까지만 테스트하면 됨
if N != 0:
    for i in range(1, 14): # 1 ~ 14
        N += 1
        if N > save_N:
            break 

        if i in [1, 6, 11]:
            result -= 1

        if N % 3 == 0:
            result += N // 3
            N = 0
            break

if N != 0:
    result = -1

print(result)