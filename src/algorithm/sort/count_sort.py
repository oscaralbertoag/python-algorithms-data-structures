def sort(to_sort, k):
    """
    Sorts a list of integers via count sort algorithm
    :param to_sort: list to sort
    :param k: upper bound for the range to be used (0 - k)
    :return: sorted copy of the original list
    """
    if len(to_sort) <= 1:
        return to_sort.copy()

    # Step 1 - count occurrences
    counts = [0] * (k + 1)
    for num in to_sort:
        counts[num] = counts[num] + 1

    for i in range(1, len(counts)):
        previous = counts[i - 1]
        current = counts[i]
        counts[i] = current + previous

    sorted_copy = [0] * len(to_sort)
    for num in to_sort:
        index_in_sorted = counts[num] - 1
        sorted_copy[index_in_sorted] = num
        counts[num] = counts[num] - 1

    return sorted_copy
