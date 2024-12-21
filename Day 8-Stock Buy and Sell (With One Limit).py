arr = [7,5,1,3,6,4]
arr = [5,4,3,2,1]
min_profit = arr[0]
profit = 0

if len(arr) < 2:  
    profit = 0

for i in range(1,len(arr)):
    if arr[i] < min_profit:
        min_profit = arr[i]
    else:
        curr_profit = arr[i] - min_profit
        if curr_profit > profit:
            profit = curr_profit

print(profit)

"""--------------------------------------------------------------------------"""
arr = [7,5,1,3,6,4]

min = arr[0]
res = 0

for i in range(1, len(arr)):
    if arr[i] < min:
        min = arr[i]
    else:
        res = max(res, arr[i] - min)
print(res)