def is_special(s):
    """
    A string is said to be a special string if either of two conditions is met:
    All of the characters are the same, e.g. aaa.
    All characters except the middle one are the same, e.g. aadaa.
    :param s: word to be checked
    :return: True if word is considered special, False otherwise
    """
    copy_s = s
    if len(s) % 2 != 0:
        middle_idx = len(s) // 2
        copy_s = s[:middle_idx] + s[middle_idx + 1:]
    for i in range(1, len(copy_s)):
        if copy_s[i] != copy_s[i - 1]:
            return False
    return True


def count_special_sub_strings(n, s):
    """
    A special substring is any substring of a string which meets one of those criteria.
    Given a string, determine how many special substrings can be formed from it.
    Example:
    s = mnonopoo contains the following special substrings: [m, n, o, n, o, p, o, o, non, ono, opo, oo]
    :param n: size of the string to analyze
    :param s: string to analyze
    :return: number of special substrings identified
    """
    cache = {}
    count = 0
    for window_size in range(n, 0, -1):
        for i in range(0, n + 1 - window_size):
            sub_str = s[i:i + window_size]
            if cache.get(sub_str):
                count += cache.get(sub_str)
            else:
                sub_str_count = 1 if is_special(sub_str) else 0
                cache[sub_str] = sub_str_count
                count += sub_str_count
    return count
