# 백준 14499

dx = [0, 0, -1, 1] # 동,서,북,남
dy = [1, -1, 0, 0]
dice = [0, 0, 0, 0, 0, 0]

def move(x, y, dir):
    nx, ny = x + dx[dir], y + dy[dir]
    if nx < 0 or nx >= n or ny < 0 or ny >= m: return False
    if dir == 0: # 동쪽
        dice[0], dice[2], dice[3], dice[5] = dice[3], dice[0], dice[5], dice[2]
    elif dir == 1: # 서쪽
        dice[0], dice[2], dice[3], dice[5] = dice[2], dice[5], dice[0], dice[3]
    elif dir == 2: # 북쪽
        dice[0], dice[1], dice[4], dice[5] = dice[4], dice[0], dice[5], dice[1]
    else: # 남쪽
        dice[0], dice[1], dice[4], dice[5] = dice[1], dice[5], dice[0], dice[4]

    if board[nx][ny] == 0: board[nx][ny] = dice[5]
    else: dice[5], board[nx][ny] = board[nx][ny], 0
    return nx, ny

n, m, x, y, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
cmd = list(map(int, input().split()))

for dir in cmd:
    result = move(x, y, dir-1)
    if result:
        x, y = result
        print(dice[0])
