"""Testing - Will not work in GFG"""
arr=[1,5,8,10]
# arr = [12,3,9,16,20]
arr.sort()
k = 2

for i in range(len(arr)):
    if arr[i] > k:
        arr[i] -= k
    else:
        arr[i] += k
print(max(arr) - min(arr))



"""Will work in GFG"""
n = len(arr)
arr.sort()
result = arr[n-1] - arr[0]
for i in range(1,n):
    if arr[i]-k < 0:
        continue
    maxHeight = max(arr[i-1] + k, arr[n-1] - k)
    minHeight = min(arr[0] + k, arr[i] - k)
    result = min(result, maxHeight - minHeight)
print(result)


