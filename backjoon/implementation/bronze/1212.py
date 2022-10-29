oct = input()
result = ""
hash = {'0' : '000', '1' : '001', '2' : '010', '3' : '011',
    '4' : '100', '5' : '101', '6' : '110', '7' : '111'}
for number in oct:
    result += hash[number]

if len(result) != 1 and result[0] == '0':
    result = result[result.find('1'):]
print(result)   

# 더 좋은 대안 -> 파이썬의 bin, oct, hex 함수 이용
# 10진수를 2진수, 8진수, 16진수로 바꿔줌
# # bin(oct)

# n = int(input(), 8)
# print(n)