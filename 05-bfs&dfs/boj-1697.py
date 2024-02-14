# 백준 1697

# Solution 1

# Get current location 
n, k = map(int, input().strip().split())

# Define Class Node
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None 
        self.teleport = None 

# Define Class Hide & Seek 
class HideAndSeek:
    def __init__(self, n):
        self.root = Node(n)
        self.height = 0 
        self.node_list = [self.root]
    
    def _onemove(self, root:Node):
        root.left = Node(root.data-1)
        root.right = Node(root.data+1)
        root.teleport = Node(root.data*2)
        
        return root.left, root.right, root.teleport
    
    def onemove(self):
        temp = []
        for node in self.node_list:
            left, right, teleport = self._onemove(node)
            temp.extend([left, right, teleport])
        self.node_list = temp
        self.height += 1
        
    def findminHeight(self, h):
        found = False
        while not found:
            self.onemove()
            if h in [node.data for node in self.node_list]:
                found = True 
        return self.height
    
hide_and_seek = HideAndSeek(n)
print(hide_and_seek.findminHeight(k))

# Solution 2

from collections import deque

MAX = 100001
n, k = map(int, input().split())
array = [0]*MAX

def bfs():
    q = deque([n])
    while q:
        now_pos = q.popleft()
        if now_pos == k:
            return array[now_pos]
        for next_pos in (now_pos-1, now_pos+1, now_pos*2):
            if 0 <= next_pos < MAX and not array[next_pos]:
                array[next_pos] = array[now_pos] + 1
                q.append(next_pos)

print(bfs())
