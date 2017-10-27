"""You're going to write a binary search function.
You should use an iterative approach - meaning
using loops.
Your function should take two inputs:
a Python list to search through, and the value
you're searching for.
Assume the list only has distinct elements,
meaning there are no repeated values, and
elements are in a strictly increasing order.
Return the index of value, or -1 if the value
doesn't exist in the list."""

def binary_search(input_array, value):

    """ Algorithm: Here is how it could be done:
    1. Get middle index of array with range (0...array-size)
    2. Compare value of mid-element at that index with given value
        2.1 If (value == mid-element)
                then return the middle index [DONE]
        2.2 Else If (value < mid-element)
                then  repeat step 1 with range (0...mid-element-index)
        2.3 Else If (value > mid-element)
                then repeat step 2 with range (mid-element-index + 1, size)
    3. Since iteration completed without finding the elements, return -1"""

    """ Step 1"""
    start = 0
    end = len(input_array)

    """ Step 2"""
    while end > start:
        mid_index = (start + end) / 2
        mid_value = input_array[mid_index]

        if value == mid_value:
            return mid_index
        elif value < mid_value:
            end = mid_index
        else:
            start = mid_index + 1

    """ Step 3"""
    return -1

test_list = [1,3,9,11,15,19,29]
test_val1 = 25
test_val2 = 15
print binary_search(test_list, test_val1)
print binary_search(test_list, test_val2)
print binary_search(test_list, 1)
print binary_search(test_list, 3)
print binary_search(test_list, 9)
print binary_search(test_list, 11)
print binary_search(test_list, 19)
print binary_search(test_list, 29)
print binary_search(test_list, 19)
print binary_search(test_list, 2)
