# p 92
N, M, K = map(int, input().split(' '))
user_list = list(map(int, input().split(' ')));
user_list.sort()
first, second = user_list[-1], user_list[-2]

count = 0
result = 0
for i in range(M):
    
    if count != K:
        count += 1
        result += first

    else:
        count = 0
        result += second

print(result)