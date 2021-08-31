# Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
#
# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

# There is an obvious quadratic solution

def checksum(numbers, ksum):
    numbers.sort()
    i = 0
    j = len(numbers) - 1
    while i != j and j != -1:
        if numbers[i] + numbers[j] < ksum:
            i = i + 1
        elif numbers[i] + numbers[j] > ksum:
            j = j - 1
        else:
            return numbers[i], numbers[j]

    return -1


print(checksum([10, 15, 3, 7], 18))
print(checksum([10, 15, 3, 7], 25))
print(checksum([10], 18))
print(checksum([], 18))
print(checksum([10], 18))

# This solution is 0(n.log n)
