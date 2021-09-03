# Given an array of integers, return a new array such that each element at index i of
# the new array is the product of all the numbers in the original array except the one at i.
#
# For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24].
# If our input was [3, 2, 1], the expected output would be [2, 3, 6].
#
# Follow-up: what if you can't use division?

# An obvious solution is O(n^2)

def p2hard(array):
    product = 1
    for item in array:
        product *= item

    for idx, val in enumerate(array):
        array[idx] = product / array[idx]

    return array


def p2hard_sol2(array):

    forward= [1] * len(array)
    backward = [1] * len(array)
    forward[0] = array[0]
    product = [1] * len(array)
    for idx, val in enumerate(array):
        if idx == 0:
            continue
        else:
            forward[idx] = array[idx] * forward[idx-1]

    backward[len(array) -1] = array[len(array) - 1]
    for idx,val in reversed(list(enumerate(array))):
        if idx == len(array)-1:
            continue
        else:
            backward[idx] = array[idx] * backward[idx + 1]

    for idx,val in enumerate(array):
        if idx == 0:
            product[0] = backward[idx +1]
        elif idx == len(array) -1:
            product[idx] = forward[len(array) - 2]
        else:
            product[idx] = forward[idx-1] * backward[idx+1]
    return product,backward,forward



print(p2hard([1, 2, 3, 4, 5]))
print(p2hard([3,2,1]))
print(p2hard([]))
print(p2hard_sol2([3,2,1]))
print(p2hard_sol2([1,2,3,4,5]))
# Solution is O(n)