import sys
input = sys.stdin.readline
INF = int(1e9)  # Set 10 billion as a value representing infinity 

# Receive the number of cities(n) and the number of buses(m) as input
n = int(input())
m = int(input())

# Create a 2D list (graph representation) and initialize all values to infinity
graph = [[INF] * (n+1) for _ in range(n+1)]

# Initialize the cost from oneself to oneself to 0
for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b:
            graph[a][b] = 0

# Receive information about each bus and initialize it to that value
for _ in range(m):
    a, b, c = map(int, input().split())
    # If the cost already set is smaller than the new cost, ignore it
    if graph[a][b] > c:
        graph[a][b] = c

# Perform the Floyd Warshall algorithm according to the recurrence relation
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# Print the resulting output
for a in range(1, n+1):
    for b in range(1, n+1):
        if graph[a][b] == INF:
            print(0, end=" ")
        else:
            print(graph[a][b], end=" ")
    print()
