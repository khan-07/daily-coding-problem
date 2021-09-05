# Given an array of integers, find the first missing positive
# integer in linear time and constant space. In other words, find the
# lowest positive integer that does not exist in the array.
# The array can contain duplicates and negative numbers as well.
#
# For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.
#
# You can modify the input array in-place.
def find_minimum(array):
    for idx, val in enumerate(array):

        if not idx == len(array) - 1:
            print(array[idx], array[idx + 1], val, array)

        if (not idx == len(array) - 1) and (array[idx + 1] > val):
            temp = array[idx + 1]
            array[idx + 1] = val
            array[idx] = temp

    print(array)


# print(find_minimum([3, 4, -1, 1]))
# print(find_minimum([1, 2, 0]))
# print(find_minimum([5, 6, -1, 2]))
print(find_minimum([6, 58, 2,4,69,67,5,1,3]))
