# 백준 1026번

# Get the length of list 
n = int(input().strip())

# Initialize a list of A, B
A = list(map(int, input().strip().split()))
B = list(map(int, input().strip().split()))

# Check if the length of A, B is n 
if len(A) != n or len(B) != n: 
    print("The length of the list doesn't match.")
    exit()
    

# Sort list A in ascending order, list B in descending order
A.sort()
B.sort(reverse=True)

# Multiply corresponding elements with same indices and sum up 
print(sum([(A[i] * B[i]) for i in range(n)]))