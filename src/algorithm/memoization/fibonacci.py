def fibonacci(n):
    """
    Calculates the requested fibonacci number recursively
    :param n: requested fibonacci number
    :return: calculated fibonacci number
    """
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


def memoized_fibonacci(n, processed):
    """
    Calculates the requested fibonacci number recursively and using memoization
    :param n: requested fibonacci number
    :param processed: map containing all previously processed fibonacci numbers
    :return: calculated fibonacci number
    """
    if n == 0:
        return 0
    if n == 1:
        return 1
    if processed.get(n) is None:
        processed[n] = memoized_fibonacci(n - 1, processed) + memoized_fibonacci(n - 2, processed)

    return processed[n]
