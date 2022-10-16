# 원래 주려고 생각했던 돈 - (받은 등수 - 1)
N = int(input())
user_input = []
for i in range(N):
    user_input.append(int(input()))

user_input.sort(reverse=True)
# 받은 등수는 점점 높아지고, 빼는 값도 점점 높아지는 구조이기 때문에
# 역으로 정렬하면 됨! 어차피 음수가 되면 0이 되기 때문에
result = 0
for i in range(N):
    tip = user_input[i] - i

    if tip > 0:
        result += tip
    
print(result)