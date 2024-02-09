# 백준 8958

# Solution 1
from typing import List

def scoreProgram(result: List[str]):
    score = [0] * len(result)
    
    for idx, ans in enumerate(result):
        if ans == 'O':
            score[idx] = score[idx - 1] + 1 if idx > 0 else 1
        else:
            score[idx] = 0
    
    return sum(score)

n = int(input().strip())
scores = []

for _ in range(n):
    my_list = list(input().strip())
    scores.append(scoreProgram(my_list))

for score in scores:
    print(score)

# Solution 2
from typing import List

def scoreProgram(result: List[str]):
    score = 0
    sum_score = 0
    
    for ans in result:
        if ans == 'O':
            score += 1
            sum_score += score
        else:
            score = 0
            
    return sum_score

n = int(input().strip())
scores = []

for _ in range(n):
    my_list = list(input().strip())
    scores.append(scoreProgram(my_list))

for score in scores:
    print(score)
