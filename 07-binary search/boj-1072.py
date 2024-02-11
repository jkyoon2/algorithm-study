# 백준 1072

# Get input
x, y = map(int, input().split())
z = (y * 100) // x

low, high = 0, 1000000000
while low <= high:
    mid = (low + high) // 2
    nx, ny = x + mid, y + mid
    nz = (ny * 100) // nx
    if nz <= z:
        low = mid + 1
    else:
        high = mid - 1

if low > 1000000000:
    print(-1)
else:
    print(low)
