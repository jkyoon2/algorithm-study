# 백준 1449번 

# Get input 
n, k = map(int, input().strip().split())

# Get leaked places and convert to list
leaks = list(map(int, input().strip().split()))

# Check if the number of leaks is correct
if len(leaks) != n:
    print("The number of leaks doesn't match. Please check again.")
    exit()

# Sort list in ascending order 
leaks.sort() 

# Tape of length k can plug up continuous k leaks in a row 
init = leaks[0]
count = 1

for i in range(1, n):
    if leaks[i] - init < k:
        continue
    else: 
        count += 1
        init = leaks[i]
        
print(count)
