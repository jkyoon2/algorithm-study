# 백준 21866

from typing import List

def coffee(score: List[int]):
    if score[0] > 100 or score[1] > 100 \
        or score[2] > 200 or score[3] > 200 \
        or score[4] > 300 or score[5] > 300 \
        or score[6] > 400 or score[7] > 400 \
        or score[8] > 500:
        return 'hacker'
    if sum(score) >= 100:
        return 'draw'
    else: 
        return 'none'
        
my_score = list(map(int, input().strip().split()))
assert(len(my_score) == 9)
print(coffee(my_score))