money = 1000 - int(input())

# 500, 100, 50, 10, 5, 1 -> greedy 적용가능
lst = [500, 100, 50, 10, 5, 1]
result = 0
for element in lst:
    result += money // element
    money %= element

print(result)