# 백준 1931 

## Solution 1 

# Import modules
from operator import itemgetter

# Get number of meetings and time schedule
n = int(input().strip()) 

meetings = []

for i in range(n):
    s, e = map(int, input().strip().split())
    meetings.append((s, e))

# Sort meeting by end time 
sortedMeetings = sorted(meetings, key = itemgetter(1, 0))

count = 0
end = 0

for i in range(n):
    if sortedMeetings[i][0] >= end:
        end = sortedMeetings[i][1]
        count += 1

print(count)