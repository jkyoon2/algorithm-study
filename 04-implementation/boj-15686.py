# 백준 15686

from itertools import combinations

# Get N, M 
n, m = map(int, input().strip().split())

# Get city information 
chicken = []
house = []

for i in range(n):
    ## [0,0,1,2,0]
    city_info = list(map(int, input().strip().split()))
    assert(len(city_info) == n)
    
    for j in range(n):
        if city_info[j] == 1:
            # [(0,2)]
            house.append((i, j))
        elif city_info[j] == 2:
            # [(0,3)]
            chicken.append((i, j))

# Define a function to calculate L1 distance
def manhattan(a, b):
    '''Function to calculate manhattan distance (L1 norm)
    
    args: 
        a, b(tuple): Location index of chicken restaurant and house
    
    return:
        L1 distance (int)
    '''
    return sum(abs(val1-val2) for val1, val2 in zip(a, b))


# Initialize minimum chicken distance as a large number
min_chicken_distance = float('inf')

# Consider all combinations of chicken houses
for chicken_houses in combinations(chicken, m):
    # Calculate city's chicken distance for this combination 
    chicken_distance = 0 
    for h in house:
        chicken_distance += min(manhattan(h, c) for c in chicken_houses)
    
    # Update minimum chicken distance 
    if chicken_distance < min_chicken_distance:
        min_chicken_distance = chicken_distance

print(min_chicken_distance)

