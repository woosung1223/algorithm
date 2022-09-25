[N, M, K] = list(map(int, input().split(' '))); # 비구조화 할당
arr = list(map(int, input().split(' ')));
# N : 배열의 길이, M : 숫자가 더해지는 횟수, K : K번 초과 불가능 (K <= M)

# greedy algorithm
# 1. 배열에서 가장 큰 요소를 찾는다
# 2. 해당 요소를 더한다
# 3. K번 초과되었다면 해당 인덱스를 제외한 다른 요소를 찾는다

def BigNumber(arr, N, M, K):
    result = 0
    idx = N - 1
    K_count = 0
    # 정렬 이용 
    arr_cp = arr.copy()
    arr_cp.sort()

    for i in range(0, M):
        if K_count == K - 1:
            result += arr_cp[idx - 1]
            K_count = 0
        else:
            result += arr_cp[idx]
            K_count += 1
    return result

print(BigNumber(arr, N, M, K))