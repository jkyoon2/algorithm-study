from typing import List

# Get input
n = int(input().strip())

# Initialize weight list 
weight_list = list(map(int, input().strip().split()))

# Initialize Binary Tree Node Class 
class Node:
    '''Basic node with left, right child initialized as None
    
        val
     ┌───┴───┒
    left    right
    
    '''
    
    def __init__(self, data: int):
        self.val = data
        self.left = None
        self.right = None 

# Initialize Binary Tree for available weights 
class WeightTree:
    
    def __init__(self, h: int, weight: List[int]):
        self.root = Node(0)
        self.h = h 
        weight.sort()
        self.weight = weight
    
    
    def build(self):
        
        self._build(self.root, 0)
    
    def _build(self, root, height):
        
        if height < len(self.weight):
            
            root.left = Node(root.val)
            root.right = Node(root.val + self.weight[height])
            
            self._build(root.left, height+1)
            self._build(root.right, height+1)
        
        else:
            return
            
    def getAlldata(self, root, result: set):
        if root:
            result.add(root.val)
            self.getAlldata(root.left, result)
            self.getAlldata(root.right, result)
        return result
    
    __call__ = getAlldata
    
    def getMinWeight(self, weights: set):
        i = min(weights)
        while i <= max(weights):
            if i not in weights:
                return i 
            i += 1
            
        return i 


my_scale = WeightTree(n, weight_list)
my_scale.build()
result = set()
measure_weights = my_scale(my_scale.root, result)
print(my_scale.getMinWeight(measure_weights))

# Solution 2

from typing import List

# Get input
n = int(input().strip())

# Initialize weight list 
weight_list = list(map(int, input().strip().split()))
weight_list.sort()

# Initialize accumulative sum of weights
accumulative_sum = 0

for weight in weight_list:
    if weight > accumulative_sum + 1:
        break
    accumulative_sum += weight

print(accumulative_sum + 1)
