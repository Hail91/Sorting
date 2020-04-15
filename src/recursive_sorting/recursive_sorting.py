# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    i = 0
    x = 0
    for v in range(0, len(merged_arr)):
            if i >= len(arrA):
                merged_arr[v] = arrB[x]
                x += 1
            elif x >= len(arrB):
                merged_arr[v] = arrA[i]
                i += 1
            elif arrA[i] < arrB[x]:
                merged_arr[v] = arrA[i]
                i += 1
            else:
                merged_arr[v] = arrB[x]
                x += 1
    return merged_arr
#  0  1  2  3  4  5  6  7  8  9
# [1, 5, 8, 4, 2, 9, 6, 0, 3, 7] <--- Arr we're using
# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    if len(arr) <= 1:
        return arr
    middle = len(arr) // 2
    left_side = merge_sort(arr[:middle])
    right_side = merge_sort(arr[middle:])
    return merge(left_side, right_side)
merge_sort([5, 21, 3, 16, 24, 11, 2])


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
