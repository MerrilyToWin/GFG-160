class Solution:
    def getTempLargest(self, arr):
        n = len(arr)
        if n < 2:
            return -1
        maxi = temp = float('-inf')
        for i in arr:
            if i > maxi:
                temp = maxi
                maxi = i
            elif i > temp  and i != maxi:
                temp = i
        
        if temp == float('-inf'):
            return -1
        else:
            return temp
        
object = Solution()
arr = [1, 2, 3, 4, 5]
print(object.getTempLargest(arr)) # Expected output: 4

"""Description"""

"""Your program should print the second larget number in the array with most efficient complexity. As you can see that they for loop will run only 
once and will print the second larget number in the array"""

"""First lets check the lenght of the array is its less than 2 then its not valid length, lets store the initial value to minus infinity and 
start the execution of the loop"""