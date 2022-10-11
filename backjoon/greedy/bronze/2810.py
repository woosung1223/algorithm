N = int(input())
sit = input()
result = 0
# LL 우선순위 부여
lst = []
temp = ""
for character in sit:
    if character == 'S':
        temp += character
        lst.append(temp)
        temp = ""
    else:
        temp += 'L'
        if temp == 'LL':
            lst.append(temp)
            temp = ""

result += lst.count('S')
if 'LL' in lst:
    result += lst.count('LL') + 1
print(result)