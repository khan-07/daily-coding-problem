# Given an array of integers, find the first missing positive
# integer in linear time and constant space. In other words, find the
# lowest positive integer that does not exist in the array.
# The array can contain duplicates and negative numbers as well.
#
# For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.
#
# You can modify the input array in-place.
def find_minimum(array):
    missing = array[0] - 1
    max_positive = array[0]
    for idx, val in enumerate(array):
        if 0 < val and val == missing:
            missing = val - 1
        elif 0 < val and val != missing:
            if not missing < val -1:
                 missing = val -1

        if max_positive < val:
            max_positive = val

    return missing if missing != 0 else max_positive + 1


print(find_minimum([3, 4, -1, 1]))
print(find_minimum([1, 2, 0]))
print(find_minimum([5, 6, -1, 2]))
print(find_minimum([6,58, -1,-2,1,69,2]))
