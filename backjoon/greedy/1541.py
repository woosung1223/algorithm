string = input()

# - 부호의 위치가 중요. - 범위를 최대한 크게(다음 - 를 만나기 전까지)
num_list = []
buho_list = [] # '-' 가 어디 위치에 있는지

temp_num = ""
minus_count = 0 # 몇번째 숫자부터 빼면 되는지
for i in range(len(string)):
    if string[i] >= '0' and string[i] <= '9':
        temp_num += string[i]
    else: # 부호라면
        num_list.append(temp_num)
        temp_num = ""
        minus_count += 1
        if string[i] == '-':
            buho_list.append(minus_count)

# 남은 버퍼 처리
num_list.append(temp_num)

for i in range(len(num_list)):
    temp = 0
    if num_list[i][0] == '0':
        for character in num_list[i]:
            if character != 0:
                flag = character
                break
        start = num_list[i].index(character)
        temp = int(num_list[i][start:])
        num_list[i] = temp
    else:
        num_list[i] = int(num_list[i])

# 이 시점에서는 숫자들이 들어있는 배열 num_list와 -가 적용되기 시작할 숫자의 인덱스가 저장되어 있는
# 배열 buho_list가 존재

flag = True # True 면 더하기, False 면 빼기
result = 0
count = 0
for i in range(len(num_list)):
    if len(buho_list) != 0 and buho_list[0] == i:
        flag = False
    if flag:
        result += num_list[i]
    else:
        result -= num_list[i]

print(result)