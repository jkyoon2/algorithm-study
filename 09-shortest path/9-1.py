INF = int(1e9)

# Receive the number of nodes and the number of edges as input
n, m = map(int, input().split())
# Create a 2D list (graph representation) and initialize all values to infinity
graph = [[INF] * (n+1) for _ in range(n+1)]

# Initialize the cost from oneself to oneself to 0
for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b:
            graph[a][b] = 0

# Receive information about each edge and initialize it to that value
for _ in range(m):
    # Set the cost from A to B and from B to A to 1
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

# Receive the node X to go through and the final destination node K as input
x, k = map(int, input().split())

# Perform the Floyd Warshall algorithm according to the recurrence relation
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# Print the resulting output
distance = graph[1][k] + graph[k][x]

# If unreachable, print '-1'
if distance >= INF:
    print('-1')
# If reachable, print the shortest distance
else:
    print(distance)
