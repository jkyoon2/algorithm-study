# 백준 1331

## Solution 1 
input_data = input().strip()
col = int(ord(input_data[0])) - int(ord('A')) 
row = int(input_data[1]) - 1
steps = [(-2, -1), (-1, -2), (1, -2), (2, -1),
         (2, 1), (1, 2), (-1, 2), (-2, 1)]
map = [[0] * 6 for _ in range(6)]
map[row][col] = 1
invalid = False
start_row, start_col = row, col 

# Already visited 
# Invalid Step 
def step(col: int, row: int):
    global invalid
    # Get location to be visited 
    input_data = input().strip()
    n_col = int(ord(input_data[0])) - int(ord('A')) 
    n_row = int(input_data[1]) - 1
    # If visited, invalid
    if map[n_row][n_col] == 1:
        invalid = True
        return row, col
    # If invalid step, invalid 
    dx, dy = n_col - col, n_row - row
    if (dx, dy) not in steps:
        invalid = True 
        return row, col
    # Mark as visited 
    map[n_row][n_col] = 1
    # Update row, col 
    return n_row, n_col

for i in range(35):
    row, col = step(col, row)
    
# Check if last step returns back to starting point
if not invalid:
    if (col - start_col, row - start_row) not in steps:
        invalid = True

if invalid:
    print('Invalid')
else:
    print('Valid')

# Solution 2

def is_valid_step(col, row, n_col, n_row, map, steps):
    # If visited or invalid step, return False
    if map[n_row][n_col] == 1:
        return False
    if (n_col - col, n_row - row) not in steps:
        return False
    return True

# Get all moves in advance
moves = [input().strip() for _ in range(36)]
start_col = int(ord(moves[0][0])) - int(ord('A')) 
start_row = int(moves[0][1]) - 1

steps = [(-2, -1), (-1, -2), (1, -2), (2, -1),
         (2, 1), (1, 2), (-1, 2), (-2, 1)]
map = [[0] * 6 for _ in range(6)]
map[start_row][start_col] = 1

valid = True
col, row = start_col, start_row

for i in range(1, 36):
    n_col = int(ord(moves[i][0])) - int(ord('A')) 
    n_row = int(moves[i][1]) - 1
    if not is_valid_step(col, row, n_col, n_row, map, steps):
        valid = False
        break
    map[n_row][n_col] = 1
    col, row = n_col, n_row

# Check if last step returns back to starting point
if valid and (col - start_col, row - start_row) not in steps:
    valid = False

print('Valid' if valid else 'Invalid')
