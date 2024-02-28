import sys
import heapq

def dijkstra(n, graph, start):
    INF = int(1e9)  # Set 10 billion as a value representing infinity
    distance = [INF] * (n + 1)  # Initialize the shortest distance table to infinity
    distance[start] = 0  # Set the shortest path to the start node to 0
    queue = []
    heapq.heappush(queue, (0, start))  # Insert the start node into the queue

    while queue:  # Until the queue is empty
        dist, now = heapq.heappop(queue)  # Get the information of the node with the shortest distance

        # If the current node has already been processed, ignore it
        if distance[now] < dist:
            continue

        # Check other nodes adjacent to the current node
        for i in graph[now]:
            cost = dist + i[1]  # Calculate the cost to go to the next node

            # If the distance to move to another node via the current node is shorter
            if cost < distance[i[0]]:
                distance[i[0]] = cost  # Update the shortest distance
                heapq.heappush(queue, (cost, i[0]))  # Insert the next node into the queue

    return distance  # Return the shortest distance from the start node to each node

n = int(sys.stdin.readline())  # Receive the number of nodes as input
m = int(sys.stdin.readline())  # Receive the number of edges as input
graph = [[] for _ in range(n + 1)]  # Create a list to contain information about nodes connected to each node

# Receive all edge information
for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    # The cost to go from node a to node b is c
    graph[a].append((b, c))

start, end = map(int, sys.stdin.readline().split())  # Receive the start node and the end node as input
distance = dijkstra(n, graph, start)  # Perform Dijkstra's algorithm
