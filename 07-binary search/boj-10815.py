# 백준 10815

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        # If found, return the middle index
        if array[mid] == target:
            return mid
        # If middle value is bigger than target, search left
        elif array[mid] > target:
            end = mid - 1
        # If middle value is smaller than target, search right
        else:
            start = mid + 1
    return None

# Get number of cards 
n = int(input().strip())

# Get cards 
cards = list(map(int, input().strip().split()))
cards.sort()

# Get numbers to check
m = int(input().strip())

checks = list(map(int, input().strip().split()))

for ch in checks:
    result = binary_search(cards, ch, 0, n-1)
    if result != None:
        print(1, end=' ')
    else:
        print(0, end=' ')