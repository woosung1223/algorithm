N = int(input())
user_input = []

for i in range(N):
    user_input.append(int(input()))

# idea -> 가장 작은 값을 가진 로프부터 제거하면서 값을 비교
user_input.sort(reverse=True)
before_w_k = -1
result = 0
for i in range(N-1, -1, -1):
    lowest_val = user_input[i]
    current_w_k = lowest_val * (N - i)
    if before_w_k < current_w_k:
        result = current_w_k
    before_w_k = current_w_k
print(result)
