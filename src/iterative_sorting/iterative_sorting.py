# TO-DO: Complete the selection_sort() function below 
# ** Steps **...

# Find the smallest card. Swap it with the first card.

# Find the second-smallest card. Swap it with the second card.

# Find the third-smallest card. Swap it with the third card.

# Repeat finding the next-smallest card, and swapping it into the correct position until the array is sorted.
def selection_sort( arr ):      
    # loop through n-1 elements  [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]
    for i in range(0, len(arr) - 1):    # Loop through the array up until the last element.
        cur_index = i                   # Assign the current index of the loop to cur_index
        smallest_index = cur_index      # Assign the cur_index to the smallest_index variable. 
        for x in range(i+1, len(arr)):  # Loop over the array again, but starting at the current index position + 1. (checking the next element to the right)
            if arr[x] < arr[smallest_index]:  # if arr value at index position 'x' is 'less than' arr value at index position 'smallest_index', then...
                smallest_index = x            # Assign the value of index position 'x' to smallest_index variable
        arr[cur_index], arr[smallest_index] = arr[smallest_index], arr[cur_index] # Swap cur_index and smallest_index values with the new values.        
    return arr


# TO-DO:  implement the Bubble Sort function below
# - Loop through your array
# - Compare each element to its neighbor
# - If elements in wrong position (relative to each other, swap them)
# - If no swaps performed, stop. Else, go back to the element at index 0 and repeat step 1.

def bubble_sort( arr ):
    for x in range(0, len(arr)):  # Loop over the input array <--- Without this loop, the logic only executes once and the arr is returned.
        for i in range(0, len(arr) - 1):  # Loop over the array again stopping at the last index item
            if arr[i] > arr[i + 1]:  # If the value at arr index 'i' is greater than the value to it's right..do the following...
                arr[i], arr[i+1] = arr[i+1], arr[i] # Swap the value on the right with the value on the left                      
    return arr

# def bubble_sort( arr ):  <--- another way to write it.
#   while True:    # While true forces the following code to run until I manually break out of it.
#        done = False  # Assign a variable done to false, this will be used to check if a swap was performed, if its true, the loop will run again.
#       for i in range(0, len(arr) - 1): # Loop over the input array
#            if arr[i] > arr[i + 1]:     # If the arr index[i] is greater than the value to the right....
#               arr[i], arr[i+1] = arr[i+1], arr[i]  # Then we swap positions in the array
#                done = True   # We also set done to true, so that the loop runs again.
#        if not done:     # If done is false, then we return out the arr from the loop meaning we are done sorting.                   
#            return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr