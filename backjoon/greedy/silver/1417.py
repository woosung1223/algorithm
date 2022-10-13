N = int(input())
person_count = []

for i in range(N):
    temp = int(input())
    person_count.append(temp)

### 
# 득표수가 많은 후보의 표부터 깎아내리는 것이 효율적
# 만약 그 후보와 다른 후보가 득표수가 같아지는 시점이 있다면
# 그 시점부터는 번갈아가면서 깎는다

result = 0 
my_count = person_count[0] # 지금 나의 득표 수
person_count.sort()

where = person_count.index(my_count)
person_count = person_count[where+1:] # 자신보다 표가 적은 후보들은 없애버림

if len(person_count) != 0:
    flag = False
    while True:
        biggest = max(person_count)
        if biggest < my_count or flag:
            break

        for i in range(len(person_count)):
            if person_count[i] == biggest:
                person_count[i] -= 1
                result += 1
                my_count += 1
                if max(person_count) < my_count:
                    flag = True
                    break

print(result)