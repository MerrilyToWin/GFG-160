"""Rotate an array in counter clockwise direction"""

#My Code  - Same as Reversal algorithm but using slicing method

arr = [1,2,3,4,5,6]
n = int(input("Enter the number: "))
n = n % len(arr)
arr[:] = arr[n:] + arr[:-(len(arr)-n)]
print(arr)


#GFG Code

"""Using Juggling Algorithm"""

import math

def rotateArray(arr, d):
    n = len(arr)
    d = d % n
    cycles = math.gcd(n, d)

    for i in range(cycles):
        startEle = arr[i]
        currIndex = i
        while True:
            nextIndex = currIndex + d
            if nextIndex >= n:
                nextIndex = nextIndex - n
            if nextIndex == i:
                break
            arr[currIndex] = arr[nextIndex]
            currIndex = nextIndex
        arr[currIndex] = startEle

"""ANOTHER_ALGORITHM - REVERSAL ALGORITHM"""

# Function to rotate an array by d elements to the left
def rotateArr(arr, d):
    n = len(arr)
    d %= n
    reverse(arr, 0, d - 1)
    reverse(arr, d, n - 1)
    reverse(arr, 0, n - 1)
def reverse(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6]
    d = 2
    rotateArr(arr, d)
    for i in range(len(arr)):
        print(arr[i], end=" ")