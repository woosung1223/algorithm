# Page 313 곱하기 혹은 더하기
# Page 507 답안

string = input()

# 2 이상이면 무조건 곱하는게 이득,
# 반면 0과 1의 경우 곱하는 건 손해가 됨
# 단, 두 수 중 하나라도 1 이하면 더하고 두 수 모두 2 이상이라면 곱한다

def mult_or_add(string):
    result = 0
    for idx in range(len(string)):
        number = int(string[idx])
        if result <= 1 or number <= 1:
            result += number
        else:
            result *= number
    return result

print(mult_or_add(string))