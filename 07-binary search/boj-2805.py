# 백준 2805

# Get number of trees(N) and needed meters(M)
n, m = list(map(int, input().strip().split()))

# Get height info 
trees = list(map(int, input().strip().split()))

# Initialize start and end index for binary search
start = 0
end = max(trees)

# Iteratively search 
result = 0
while start <= end:
    total = 0
    mid = (start + end) // 2
    for tr in trees:
        if tr > mid:
            total += tr - mid
    # If we need to cut more, search left
    if total < m:
        end = mid - 1
    # If we need to cut less, search right
    else:
        result = mid 
        start = mid + 1

print(result)
