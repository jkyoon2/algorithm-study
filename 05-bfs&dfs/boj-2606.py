# 백준 2606번

from typing import List

# Get number of computers 
n = int(input().strip())

# Get the number of computer pairs directly connected by the network 
m = int(input().strip())

# Get the connected computer pairs 
graph = [[] for _ in range(n+1)]
visited = [False for _ in range(n+1)]

for i in range(m):
    a, b = map(int, input().strip().split())
    graph[a].append(b)
    graph[b].append(a)

# Define function dfs 
def dfs(graph: List[List[int]], x: int, visited: List[bool]) -> int:
    '''
    Get the number of computers in the corresponding connected component 
    
    Args: 
        graph(nested list)  : adjacency list of computer network graph 
        x(int)              : computer index (1, 2, ..., n)    
        visited(list)       : marked True if the computer with corresponding index is visited
    
    Return: 
        num(int) : number of computers within the connected component 
    '''
    # Mark current node as visited 
    visited[x] = True
    count = 0
    # Visit current node and adjacent nodes recursively 
    for i in graph[x]:
        if not visited[i]:
            count += dfs(graph, i, visited)
            
    return count 

dfs(graph, 1, visited)
true_count = visited.count(True)
print(true_count-1)