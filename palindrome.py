def is_palindrome(value: str) -> bool:
    """
    This function determines if a word or phrase is a palindrome

    :param value: A string
    :return: A boolean
    """
    test = value.lower().replace(' ', '')
    i = 0
    j = len(test) - 1
    while i < j:
        if test[i] != test[j]:
            return False
        i += 1
        j -= 1
    return True