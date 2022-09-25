N, K = map(int, input().split(' '))

def makeOne(N, K):
    result = 0
    while N // K != 0:
        while N % K != 0:
            N -= 1
            result += 1
        N = N / K
        result += 1
    return result

print(makeOne(N, K))