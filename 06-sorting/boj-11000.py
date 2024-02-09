# 백준 11,000번 

## Solution 1 : O(n^2) -> iter through the whole list, inefficient 

# Get number of meetings 
n = int(input().strip())

# Initialize an empty list for starting time, ending time 
start = []
end = []

for _ in range(n):
    a, b = map(int, input().strip().split())
    start.append(a)
    end.append(b)

# Check the length of start, end list is n
if len(start) != n or len(end) != n: 
    print("Number of meetings don't match.")
    exit()

# Initialize count list 
count = [0] * max(end)

# Increment index of the data 
for i in range(n):
    for j in range(start[i], end[i]):
        count[j] += 1 

# Print the maximum value in the count list 
print(max(count))

## Solution 2 -> Greedy algorithm : use min heap 

import heapq

n = int(input())
classes = []
for _ in range(n):
    s, e = map(int, input().split())
    classes.append((s, e))

# Sort by start time, then by end time
classes.sort()

# Initialize heap
heap = []
heapq.heappush(heap, classes[0][1])

for i in range(1, n):
    if heap and classes[i][0] >= heap[0]: 
        heapq.heappop(heap)
    heapq.heappush(heap, classes[i][1])

print(len(heap))
