# 백준 14503

# Get room size 
n, m = map(int, input().strip().split())

# Get the robot's current location and direction 
y, x, dir = map(int, input().strip().split())

# Get room state 
room = [list(map(int, input().strip().split())) for _ in range(n)]

# Define direction (0: North, 1: East, 2: South, 3: West)
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def is_range(x, y):
    if (0 <= x < n) and (0 <= y < m):
        return True
    return False

# Define a function to change the global variable direction (left)
def turn_left():
    global dir
    dir -= 1 
    if dir == -1:
        dir = 3

# Mark current coordinate as cleaned 
room[x][y] = 2
count = 1

# Initialize turn time as 0
turn_time = 0

while True:
    # turn left 
    turn_left()
    # Get the potential coordinates
    nx = x + dx[dir]
    ny = y + dy[dir]
    # If the coordinate is within the range and blank 
    if is_range(nx, ny) and room[nx][ny] == 0:
        # Clean it 
        room[nx][ny] = 2
        count += 1
        # Move the robot cleaner
        x, y = nx, ny
        # Initialize turn time 
        turn_time = 0
        continue
    else:
        turn_time += 1
    # If the surrounding coordinates are all cleaned
    if turn_time == 4:
        # Go back 
        nx = x - dx[dir]
        ny = y - dy[dir]
        # If possible and within the range
        if is_range(nx, ny) and room[nx][ny] == 2:
            x, y = nx, ny
        else: 
            break 
        turn_time = 0

print(count)
