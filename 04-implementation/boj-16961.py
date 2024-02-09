# 백준 16961

## Solution 1 

# Get number of inputs 
n = int(input().strip())

# Define a function counting the number of guests for each day 
def termOccupation(start: int, end: int, 
                   count: list[int]):
    ## '151', '307'
    for i in range(start-1, end):
        count[i] += 1
    
    return count
    

# Initialize list of Tab guests and Space guests 
## t_count = [0] * 366
## s_count = [0] * 366

t_count = [0]*366
s_count = [0]*366
longest = 0

# Iterate loop to count the number of guests for each day 
for i in range(n):
    guest_info = input().strip().split()
    if guest_info[0] == 'T':
        ## ['T', '151', '307']
        t_count = termOccupation(int(guest_info[1]), int(guest_info[2]), t_count)
    else: 
        s_count = termOccupation(int(guest_info[1]), int(guest_info[2]), s_count)
    longest = max(longest, int(guest_info[2]) - int(guest_info[1]) + 1)

# 1, 2 
## Make a list of total guests 
total_guests = [t_count[i] + s_count[i] for i in range(366)]
empty_days = total_guests.count(0)
print(366-empty_days)
print(max(total_guests))

# 3
no_fight = [True if t_count[i] == s_count[i] and t_count[i] != 0 else False for i in range(366)]
print(no_fight.count(True))  

# 4
no_fight_max = 0
if no_fight.count(True) > 0:
    for i, noFight in enumerate(no_fight):
        if noFight: 
            no_fight_max = max(no_fight_max, total_guests[i])
    print(no_fight_max)  
else:
    print(0)
    
# 5
print(longest)
    
# Solution 2

# Get number of inputs 
n = int(input().strip())

# Define a function counting the number of guests for each day 
def termOccupation(start: int, end: int, count: list[int]):
    for i in range(start-1, end):
        count[i] += 1

# Initialize list of Tab guests and Space guests 
t_count = [0]*366
s_count = [0]*366
longest = 0

# Iterate loop to count the number of guests for each day 
for _ in range(n):
    guest_info = input().strip().split()
    start, end = int(guest_info[1]), int(guest_info[2])
    if guest_info[0] == 'T':
        termOccupation(start, end, t_count)
    else: 
        termOccupation(start, end, s_count)
    longest = max(longest, end - start + 1)

# Make a list of total guests and calculate empty days in one pass
total_guests = []
occupied_days = 0
max_guests = 0
for i in range(366):
    guests_today = t_count[i] + s_count[i]
    total_guests.append(guests_today)
    if guests_today > 0:
        occupied_days += 1
    max_guests = max(max_guests, guests_today)

print(occupied_days)
print(max_guests)

# Calculate no fight days and max guests on no fight days
no_fight_days = 0
no_fight_max_guests = 0
for i in range(366):
    if t_count[i] == s_count[i] and t_count[i] != 0:
        no_fight_days += 1
        no_fight_max_guests = max(no_fight_max_guests, total_guests[i])

print(no_fight_days)
print(no_fight_max_guests)

# Print the longest stay
print(longest)
