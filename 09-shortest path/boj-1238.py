import heapq
import sys

def dijkstra(start):
    heap_data = []
    heapq.heappush(heap_data, (0, start))
    distance[start] = 0
    while heap_data:
        dist, now = heapq.heappop(heap_data)
        if distance[now] < dist:
            continue
        for i in adj[now]:
            cost = dist + i[1]
            if distance[i[0]] > cost:
                distance[i[0]] = cost
                heapq.heappush(heap_data, (cost, i[0]))

n, m, x = map(int, input().split())
INF = int(1e9)
adj = [[] for _ in range(n + 1)]
distance = [INF] * (n + 1)

# Store all edge information
for _ in range(m):
    start, end, time = map(int, sys.stdin.readline().split())
    adj[start].append((end, time))

# Perform Dijkstra's algorithm for the party location
dijkstra(x)
result = distance[:]

# Perform Dijkstra's algorithm for each student's home
for i in range(1, n + 1):
    if i == x:
        continue
    distance = [INF] * (n + 1)
    dijkstra(i)
    result[i] += distance[x]

print(max(result[1:]))
