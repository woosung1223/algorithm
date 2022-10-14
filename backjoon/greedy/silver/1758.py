# 원래 주려고 생각했던 돈 - (받은 등수 - 1)
N = int(input())
user_input = []
for i in range(N):
    user_input.append(int(input()))

user_input.sort()

result = 0
for i in range(N):
    tip = user_input[i] - i

    if tip > 0:
        result += tip
    
print(result)