# 백준 1654

# Get number of LAN cable given (K) and LAN cable needed (N)
k, n = list(map(int, input().strip().split()))

# Get the length of each LAN cable 
cables = [int(input().strip()) for _ in range(k)]

# Initialize start and end index for binary search 
start = 1
end = max(cables)

# Iteratively search 
result = 0 

while start <= end:
    total = 0
    mid = (start + end) // 2
    for cb in cables:
        total += cb // mid
    if total < n:
        end = mid - 1
    else: 
        result = mid
        start = mid + 1

print(result)