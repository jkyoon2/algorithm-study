# 백준 1541

## Solution 1 
from functools import reduce

# Get input 
input_str = input().strip()

# Separate input string with terms that should be added

## ['55','50+40']
split_1 = input_str.split('-')

## [['55'],['50','40']]    
split_2 = [i.split('+') for i in split_1]
    
# Sum positive integers in the nested list 
## [55, 90]
sum_list = []
for split_3 in split_2:
    sum_list.append(sum(map(int, split_3)))

# Subtract positive integers using built-in module reduce 
result = reduce(lambda x, y: x - y, sum_list)
# result = sum_list[0] - sum(sum_list[1:])

print(result)
