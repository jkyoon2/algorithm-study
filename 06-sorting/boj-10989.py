from collections import defaultdict
N = int(input())

count_dict = defaultdict(int)
max_num = 0
for _ in range(N):
    num = int(input())
    count_dict[num] += 1
    if max_num < num:
        max_num = num  
    
for num in range(max_num+1):
    if count_dict[num] != 0:
        for j in range(count_dict[num]):
            print(num)

