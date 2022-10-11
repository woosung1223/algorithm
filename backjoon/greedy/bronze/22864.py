from cmath import pi


A, B, C, M = map(int, input().split(' '))

# 일하면 피로도는 A 만큼 쌓이고 일은 B만큼 처리 가능
# 한시간 쉬면 피로도는 C 만큼 줄어듬, 0 이상
# 피로도는 M을 넘어가면 안됨
# 24시간 최대로 일을 하면 몇시간?

result = 0 # 일한 시간 양

# IDEA -> 일할 수 있는 만큼만 쉬어라
piro_count = 0
for i in range(24):
    if piro_count + A <= M:
        piro_count += A
        result += B
    else:
        piro_count -= C
        if piro_count < 0:
            piro_count = 0
        
print(result)