# 백준 11399

## Solution 1 

# Get number of people 
n = int(input().strip()) 

# Get corresponding time needed to deposit money 
## [3, 1, 4, 3, 2]
time_list = list(map(int, input().strip().split()))

# Sort in ascending order 
## [1, 2, 3, 3, 4]
time_list.sort()

# Add total amount of time 
## [1*5, 2*4, 3*3, 3*2, 4*1]
total = [time * (n-idx) for idx, time in enumerate(time_list)]
## 32
result = sum(total)    

print(result)
