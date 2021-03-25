def is_palindrome(s):
    """
    A palindrome is a word, number, phrase, or other sequence of characters which reads the same backward as forward.
    This method determines whether the provided string is a palindrome or not
    :param s: string to analyze
    :return: True if provided string is a palindrome; False otherwise
    """
    s_copy = s.replace(" ", "")
    n = len(s_copy)
    for i in range(n // 2):
        left = s_copy[i]
        right = s_copy[n - 1 - i]
        if left.upper() != right.upper():
            return False
    return True
