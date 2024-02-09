# 백준 5585 

## Solution 1 

# Get input 
## 380 
price = int(input().strip())
## 620
change = 1000 - price 

## Give as many coins possible
coin_list = [500, 100, 50, 10, 5, 1]
count = 0
for coin in coin_list:
    count += change // coin
    change %= coin

print(count)