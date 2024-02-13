# 백준 2343

# 9 3
# 1 2 3 4 5 6 7 8 9

# Get number of lectures (N) and number of Blu-ray discs (M)
N, M = map(int, input().split())

# Get the length of each lecture
lectures = list(map(int, input().split()))

# Initialize start and end index for binary search
start = max(lectures)
end = sum(lectures)

# Iteratively search
result = 0
while start <= end:
    mid = (start + end) // 2
    total = 0
    count = 0
    for lecture in lectures:
        if total + lecture > mid:
            total = 0
            count += 1
        total += lecture
    if total > 0:
        count += 1
    if count > M:
        start = mid + 1
    else:
        result = mid
        end = mid - 1

print(result)
