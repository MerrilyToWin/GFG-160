#Move all the zeroes in the end of the array 
arr = [1,2,0,4,3,0,5,0]
count = 0
for i in range(len(arr)):
    if arr[i]!=0:
        arr[count],arr[i] = arr[i],arr[count]
        count += 1
print(arr)

"""Description"""

"""You need to write a program to move all the zeros in the end of the given array. The program should have a time complexity of O(n) and 
should not use any extra space. As you can see, the program uses a single for loop to iterate through the array and swaps non-zero elements
 with the zeros. The count variable keeps track of the index where the next non-zero element should be placed. The program also handles the 
 case where the array contains negative numbers. The program should still move all the zeros to the end of the array while maintaining the 
 relative order of the non-zero elements. """