import heapq 
import sys 
input = sys.stdin.readline 
INF = int(1e9)  # Set 10 billion as a value representing infinity 

# Receive the number of nodes and the number of edges as input
n, m = map(int, input().split())
# Receive the number of the start node as input
start = int(input())
# Create a list to contain information about nodes connected to each node
graph = [[] for i in range(n+1)]
# Initialize the shortest distance table to infinity
distance = [INF] * (n+1)

# Receive all edge information
for _ in range(m):
    a, b, c = map(int, input().split())
    # The cost to go from node a to node b is c
    graph[a].append((b, c))

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

# Print the shortest distance to all nodes
for i in range(1, n+1):
    # If unreachable, print "INFINITY"
    if distance[i] == INF:
        print("INFINITY")
    # If reachable, print the distance
    else:
        print(distance[i])
