# Page 111 상하좌우

N = int(input())
where = input().split(' ')

def LRUD(N, where):
    # N x N 
    result = [1,1]

    for element in where:
        if element == 'L' and result[1] > 1:
            result[1] -= 1
        elif element == 'R' and result[1] < N:
            result[1] += 1
        elif element == 'U' and result[0] > 1:
            result[0] -= 1
        elif element == 'D' and result[0] < N:
            result[0] += 1
    
    return result

print(LRUD(N, where))