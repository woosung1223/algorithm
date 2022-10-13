# greedy -> A 부터 적용, 안되면 B 적용, 안되면 -1
# XXXX 를 먼저 찾고 다 변환, 이후에 XX를 찾고 다 변환. 그래도 X가 남아있다면 -1
# .은 마지막에 위치만 찾아서 넣어준다
board = input()

board = board.replace('XXXX', 'AAAA')
board = board.replace('XX', 'BB')
if 'X' in board:
    board = -1

print(board)

# 이런 방식도 있음 !
# n = input()
# n = n.split('.')
# new = ""
# for i in n:
#     if len(i) % 2 != 0:
#         print(-1)
#         break
#     a = int(len(i)//4)
#     b = int((len(i)%4)/2)
#     new += "AAAA" * a
#     new += "BB" * b
#     new += '.'
# else:
#     print(new[:-1])

# 우선 .을 기점으로 split 한다.
# 이후 각 요소를 체킹하면서 길이가 2의 배수가 아니라면 -1
# a는 AAAA 이므로 4로 나눈 몫이고, b는 4로 나눈 나머지 // 2 이다
# 여기도 AAAA 먼저 체킹한다는 greedy 개념이 적용됨
