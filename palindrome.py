def is_palindrome(value: str) -> bool:
    """
    This function determines if a word or phrase is a palindrome

    :param value: A string
    :return: A boolean
    """
    upperValue = value.upper()
    reverseStr = upperValue[::-1]
    if upperValue == reverseStr:
        return True
    else:
        return False  # remove pass statement and implement me

print(is_palindrome('radar'))
