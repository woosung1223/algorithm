N = int(input())
muscle_loss = list(map(int, input().split(' ')))

# idea -> 근손실의 최대치를 최소로 하게하는 값
# 짝수개라면 정렬 후 끝과 끝을 더해주면 됨
# 홀수개라면 마지막 원소는 제외하고 위 과정 수행
muscle_loss.sort()

last_loss = muscle_loss[-1]
biggest_loss = 0
if N % 2 != 0:
    N -= 1

for i in range(N):
    sum_loss = muscle_loss[N-i-1] + muscle_loss[i]
    if sum_loss > biggest_loss:
        biggest_loss = sum_loss

if N % 2 != 0:
    biggest_loss = max(last_loss, biggest_loss)

print(biggest_loss)