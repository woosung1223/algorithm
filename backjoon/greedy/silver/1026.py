N = int(input())
A = list(map(int, input().split(' ')))
B = list(map(int, input().split(' ')))

# A는 유동, B는 고정
# B의 작은 건 큰거와, A의 큰건 B의 작은거와 매핑
# A는 sort, B는 반대로 sort
A.sort()
B.sort(reverse=True)

result = 0
for i in range(N):
    result += A[i] * B[i]


print(result)