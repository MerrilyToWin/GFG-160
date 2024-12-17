#Reverse an array
arr = [1,2,3,4,5,6]

start = 0
end = len(arr) -1
for i in range(end):
    arr[start], arr[end] = arr[end], arr[start]
    start +=1
    end -= 1
print(arr)


"Another example"

class Solution:
    def reverseArray(self, arr):
        n=len(arr)
        for i in range(n//2):
            temp = arr[i]
            arr[i] = arr[n-i-1]
            arr[n-i-1] = temp
        return arr
    
# Test the solution

arr = [1,2,3,4,5,6]
print(Solution().reverseArray(arr)) # Expected output: [6, 5, 4, 3, 2, 1]

"""Description"""

"""Your program should reverse the given array in-place and return the reversed array. As you can see that the 
solution uses a simple two-pointer approach to swap elements from the start and end of the array, resulting in 
an efficient solution with a time complexity of O(n)."""

"""Example:
Input: [1, 2, 3, 4, 5, 6]
Output: [6, 5, 4, 3, 2, 1]
"""
