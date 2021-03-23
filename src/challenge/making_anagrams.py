def find_character_frequencies(word):
    """
    Builds a map with character-to-character-count found in a string
    :param word: to analyze
    :return: character-to-character-count map
    """
    frequencies = {}
    for c in word:
        frequencies[c] = frequencies.get(c, 0) + 1
    return frequencies


def calculate_minimum_deletions(a, b):
    """
    A student is taking a cryptography class and has found anagrams to be very useful.
    Two strings are anagrams of each other if the first string's letters can be rearranged to form the second string.
    In other words, both strings must contain the same exact letters in the same exact frequency.
    For example, bacdc and dcbac are anagrams, but bacdc and dcbad are not.
    The student decides on an encryption scheme that involves two large strings.
    The encryption is dependent on the minimum number of character deletions required to make the two strings anagrams.
    Determine this number.
    Given two strings, a and b, that may or may not be of the same length, determine the minimum number of character
     deletions required to make a and b anagrams. Any characters can be deleted from either of the strings.
    :param a: first string
    :param b: second string
    :return: minimum number of character deletions required to make the two strings anagrams.
    """
    deletions = 0
    chars_a = find_character_frequencies(a)
    chars_b = find_character_frequencies(b)

    processed_chars = {}
    for key in list(chars_a.keys()) + list(chars_b.keys()):
        if not processed_chars.get(key):
            deletions += abs(chars_a.get(key, 0) - chars_b.get(key, 0))
            processed_chars[key] = key

    return deletions
