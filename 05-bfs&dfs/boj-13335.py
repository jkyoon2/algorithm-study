# 백준 13335번 

from collections import deque

# Get n, w, L inputs separated by a space 
n, w, L = map(int, input().strip().split())

# Get the weight of trucks separated by a space and make it into a list 
trucks = list(map(int, input().strip().split()))

# Initialize a queue for bridge which has the weight of truck as corresponding element 
bridge = deque([0] * w) # Initialize as [0, 0]

# Keep track of bridge_weight, time 
bridge_weight = 0
time = 0 

# Each truck crosses the bridge in the given order 
for truck in trucks: 
    while True: 
        bridge_weight -= bridge[0]      # Truck finishes crossing bridge
        bridge.popleft()                # Dequeue (FIFO) 
        if bridge_weight + truck <= L:  # If a truck can go up the bridge
            bridge.append(truck)
            bridge_weight += truck 
            time += 1
            break 
        else:                           # If not 
            bridge.append(0)
        time += 1 

# Print the total time 
print(time + w)                         # Should consider the time for the last truck to cross the bridge
            
            
