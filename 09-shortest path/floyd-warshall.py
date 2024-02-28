INF = int(1e9)  # Set 10 billion as a value representing infinity 

# Receive the number of nodes and the number of edges as input
n = int(input())
m = int(input())
# Create a 2D list (graph representation) and initialize all values to infinity
graph = [[INF] * (n+1) for _ in range(n+1)]

# Initialize the cost of going from oneself to oneself to 0
for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b:
            graph[a][b] = 0 

# For each edge, receive information and initialize its value
for _ in range(m):
    # Set the cost of going from A to B to C
    a, b, c = map(int, input().split())
    graph[a][b] = c

# Perform Floyd Warshall algorithm according to the recurrence relation
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# Print the results
for a in range(1, n+1):
    for b in range(1, n+1):
        # If unreachable, print "INFINITY"
        if graph[a][b] == INF:
            print("INFINITY", end=" ")
        # If reachable, print the distance
        else:
            print(graph[a][b], end=" ")
    print()
