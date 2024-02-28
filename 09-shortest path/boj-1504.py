import heapq
import sys

def dijkstra(start):
    heap_data = []  # Initialize an empty heap
    heapq.heappush(heap_data, (0, start))  # Push the start node into the heap
    distance[start] = 0  # The distance from the start node to itself is 0
    while heap_data:  # While the heap is not empty
        dist, now = heapq.heappop(heap_data)  # Pop a node from the heap, set it as the current node

        # If the calculated shortest distance for the current node is less than the popped distance, ignore this node
        if distance[now] < dist:
            continue

        # Calculate the cost of moving to adjacent nodes through the current node
        for i in graph[now]:
            cost = dist + i[1]

            # If the calculated cost is less than the current shortest distance to the adjacent node
            if distance[i[0]] > cost:
                distance[i[0]] = cost  # Update the shortest distance
                heapq.heappush(heap_data, (cost, i[0]))  # Push the adjacent node into the heap

    return distance  # Return the shortest distance from the start node to each node

n, e = map(int, input().split())
INF = int(1e9)
graph = [[] for _ in range(n + 1)]
distance = [INF] * (n + 1)

for _ in range(e):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

v1, v2 = map(int, sys.stdin.readline().split())

result = []

# Perform Dijkstra's algorithm for nodes 1, v1, and v2
for i in [1, v1, v2]:
    dijkstra(i)
    result.append(distance[:])
    distance = [INF] * (n + 1)

# Calculate the minimum of the shortest paths passing through nodes v1 and v2 in both orders
answer = min(result[0][v1] + result[1][v2] + result[2][n], result[0][v2] + result[2][v1] + result[1][n])

# If the shortest path is infinity (i.e., the path doesn't exist), print -1. Otherwise, print the shortest path.
print(answer if answer < INF else -1)
