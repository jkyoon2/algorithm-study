# 백준 2720

## Solution 1 

coin_list = [25, 10, 5, 1]

def change(x: int) -> str:
    '''
    Function returning number of quarters, dimes, nickels, pennies
    
    args:
        x(int) : change
    
    return: 
        numbers: '1 2 3 4'
    '''
    # Get input 
    ## 124
    
    # Give as many coins at the given moment 
    ## [4, 2, 0, 4]
    for_liam = []
    for coin in coin_list:
        for_liam.append(x // coin)
        x %= coin
    
    # Print output 
    ## '4 2 0 4'
    result = ' '.join(map(str, for_liam))
    return result

n = int(input().strip())

results = [change(int(input().strip())) for _ in range(n)]

for result in results:
    print(result)
    