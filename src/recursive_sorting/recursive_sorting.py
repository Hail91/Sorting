# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge( arrA, arrB ):   # Define a function called merge, takes 2 lists as arguments.
    elements = len( arrA ) + len( arrB )   # define a variable elements that gets the result of adding the length of the 2 lists passed in as arguments to the function.
    merged_arr = [0] * elements # define a list merged_arr that will contain all zeroes initially, and be equal to the length of the 2 arrs passed into the function as arguments.
    i = 0   # Initialize a variable 'i' to zero, this will be used to track the data for the left_side array/list.
    x = 0   # Initialize a variable 'x' to zero, this will be used to track the data for the right_side array/list.
    for v in range(0, len(merged_arr)): # Loop over the merged_arr incrementing v by 1 on each pass.
            if i >= len(arrA):  # Check if value of i is greater than or equal to the length of left_side array, if it is....
                merged_arr[v] = arrB[x] # Then assign the value of right_side arr at index[i] to merged arr at index[v]
                x += 1 # increment x by 1
            elif x >= len(arrB): # Otherwise, check if value of x is greater than or equal to the length of right_side arr, if it is...
                merged_arr[v] = arrA[i] # Assign value of left_side arr at index[i] to merged_arr at index[v].
                i += 1 # increment i by 1
            elif arrA[i] < arrB[x]: # Otherwise, check if value of left_side arr at index[i] is less than right_side arr at index[x], if it is...
                merged_arr[v] = arrA[i] # Assign value of left_side arr at index[i] to merged_arr at index[v].
                i += 1 # increment i by 1.
            else:
                merged_arr[v] = arrB[x] # Otherwise, if all other prior checks fail, assign the value of right_side at index[x] to merged arr at index[v]/
                x += 1 # increment x by 1.
    return merged_arr # Return the merged arr out of the function.
#  0  1  2  3  4  5  6  7  8  9
# [1, 5, 8, 4, 2, 9, 6, 0, 3, 7] <--- Arr we're using
# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ): # Define function taking in a list as an argument
    if len(arr) <= 1:  # This is our base case to exit the recursion, if length of the input arr is less than or equal to 1, then return out the arr.
        return arr
    middle = len(arr) // 2  # Get the middle element of the input arr 
    left_side = merge_sort(arr[:middle]) # Run the function again recursively on only the left side the array. It will keep re-running this until the 'left_side' of input arr is length 1                                     #
    right_side = merge_sort(arr[middle:]) # Then it will hit this line and run the function recursively on the RIGHT side of the input arr, it will do this until the 'right_side' of input arr is length 1
    return merge(left_side, right_side)   # Once both left and right side are length of 1, it will return the result of running the merge function with the left/right side arr's passed in as arguments
merge_sort([1, 5, 8, 4, 2, 9, 6, 0, 3, 7])  # <---Using this to run the code in python tutor to help visualize the execution.


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
