# 변환될 수 있는 수 중 가장 큰 값과 작은 값
MK_string = input()

# idea -> MK를 모두 조합하면 큰 수, M 과 K를 모두 분리하면 작은 수
# 단 마지막에 MM이 오는 경우는? 11로 해석해야 함. 10이 아니라. 최댓값에서

result_max_str = ''
result_min_str = ''

# 최대 수
buffer = ""   
for character in MK_string:
    buffer += character
    if character == 'K':
        # flush
        
        M_count = buffer.count('M')
        result_max_str += str(5 * 10 ** M_count)
        buffer = ""
if buffer != "": # MM 꼴이 남아 있다면
    result_max_str += '1' * (buffer.count('M'))

# 최소 수

buffer = ""   
for character in MK_string:
    if character == 'K':
        # flush
        
        M_count = buffer.count('M')
        if M_count > 0:
            result_min_str += str(1 * 10 ** (M_count - 1))
        result_min_str += '5'
        buffer = ""
    else:
        buffer += 'M'

if buffer != "": #  MM 꼴이 남아 있다면
    result_min_str += str(1 * 10 ** (buffer.count('M') - 1))
print(result_max_str)
print(result_min_str)