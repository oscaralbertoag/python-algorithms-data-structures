def find_longest_sequence(numbers):
    """
    This function iterates over the provided list and returns the longest continuous sequence. For example, if the list
    [7,1,2,11,12,13] was provided, it contains sequences [1,2] and [11,12,13]. This method would return the latter.
    :param numbers: list to inspect for sequences (no repeated elements exist, and all elements should be valid integers)
    :return: longest sequence available (smallest sequence possible is of size 2)
    """
    numbers_copy = numbers.copy()
    numbers_copy.sort()
    longest = []
    current = []

    for i in range(1, len(numbers_copy)):
        if numbers_copy[i] - numbers_copy[i - 1] == 1:
            if len(current) == 0:
                current += [numbers_copy[i - 1], numbers_copy[i]]
            else:
                current.append(numbers_copy[i])
            if len(current) > len(longest):
                longest = current[:]
        else:
            if len(current) > len(longest):
                longest = current[:]
            current.clear()
    return longest
