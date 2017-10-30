def exchange(input_array, index1, index2):
        temp = input_array[index1]
        input_array[index1] = input_array[index2]
        input_array[index2] = temp

def is_sorted(input_array):
    end = len(input_array)
    for index in range(0, end - 1):
        if input_array[index] > input_array[index + 1]:
            return False
    return True

def bubble_sort(input_array):
    """ Algorithm:
    1. Compare two adjacent numbers, move the large one towards left
    2. Do above process for all the numbers(Pass)
    3. Repeat step 1 till all the numbers are sorted.
    """
    end = len(input_array)
    start = 0;

    # if array is already sorted no need to run Sorting Algo
    if is_sorted(input_array):
        print "Already Sorted! No need to sort."
        return

    # Bubble Sort
    for outer_index in range(start, end):
        for index in range(0, end - 1):
            if input_array[index] > input_array[index + 1]:
                exchange(input_array, index, index + 1)
        start += 1

#test0
array = []
bubble_sort(array)
print array," Is sorted? -->", is_sorted(array)

#test1
array = [1]
bubble_sort(array)
print array," Is sorted? -->", is_sorted(array)

#test2
array = [1, 2, 3, 4, 5, 10, 9, 8, 7]
print array," Is sorted? -->", is_sorted(array)
bubble_sort(array)
print array," Is sorted? -->", is_sorted(array)

#test3
array = [1, 2, 3, 4, 5, 6, 7]
print array," Is sorted? -->", is_sorted(array)
bubble_sort(array)
print array," Is sorted? -->", is_sorted(array)

#test4
array = [1, 2, 3, 4, 5, 6, 7]
array.reverse()
print array," Is sorted? -->", is_sorted(array)
bubble_sort(array)
print array," Is sorted? -->", is_sorted(array)
