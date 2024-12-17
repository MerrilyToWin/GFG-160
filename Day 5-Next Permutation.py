"""Nest Permutation"""

# "My code"
def next_permutation(arr):
    n = len(arr)
    i = n - 2
    while i >= 0 and arr[i] >= arr[i + 1]:
        i -= 1
    
    if i >= 0:
        j = n - 1
        while arr[j] <= arr[i]:
            j -= 1
        arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1:] = reversed(arr[i + 1:])


# "GFG Code"

def permutations(res, arr, idx):
    
    # Base case: if idx reaches the end of the list
    if idx == len(arr) - 1:
        res.append(arr[:])
        return

    # Generate permutations by swapping each
    # element starting from index idx
    for i in range(idx, len(arr)):
        
        # Swapping
        arr[idx], arr[i] = arr[i], arr[idx]

        # Recursive call to create permutations 
        # for the next element
        permutations(res, arr, idx + 1)

        # Backtracking
        arr[idx], arr[i] = arr[i], arr[idx]


def next_permutation(arr):
    
    # Begin with the smallest permutation
    curr = arr[:]

    # Generate all permutations and store in res
    res = []
    permutations(res, curr, 0)
    res.sort()

    # Traverse through res and print the next permutation
    for i in range(len(res)):
        
        # Found a match
        if res[i] == arr:
            
            # Print next
            if i < len(res) - 1:
                arr[:] = res[i + 1]
                
            else:
                
                # If the given permutation is 
                # the last
                arr[:] = res[0]
            
            break


if __name__ == "__main__":
    arr = [2, 4, 1, 7, 5, 0]
    next_permutation(arr)
    print(" ".join(map(str, arr)))

