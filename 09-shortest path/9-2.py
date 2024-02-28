import heapq 
import sys 

input = sys.stdin.readline 
INF = int(1e9)  # Set 10 billion as a value representing infinity 

# Receive the number of nodes, the number of edges, and the start node as input
n, m, start = map(int, input().split())

# Create a list to contain information about nodes connected to each node
graph = [[] for i in range(n+1)]
# Initialize the shortest distance table to infinity
distance = [INF] * (n+1)

# Receive all edge information
for _ in range(m):
    x, y, z = map(int, input().split())
    # The cost to go from node x to node y is z
    graph[x].append((y, z))

def dijkstra(start):
    q = []
    # Set the shortest path to the start node to 0 and insert it into the queue
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:    # Until the queue is empty
        # Get the information of the node with the shortest distance
        dist, now = heapq.heappop(q)
        # If the current node has already been processed, ignore it
        if distance[now] < dist:
            continue 
        # Check other nodes adjacent to the current node
        for i in graph[now]:
            cost = dist + i[1]
            # If the distance to move to another node via the current node is shorter
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

# Perform Dijkstra's algorithm
dijkstra(start)

# The number of nodes that can be reached 
count = 0 
# Among the nodes that can be reached, the shortest distance to the farthest node
max_distance = 0
for d in distance:
    # In case it's a reachable node
    if d != INF:
        count += 1
        max_distance = max(max_distance, d)

# The start node should be excluded, so print count-1 
print(count-1, max_distance)
