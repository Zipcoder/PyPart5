def is_palindrome(value: str) -> bool:
    """
    This function determines if a word or phrase is a palindrome

    :param value: A string
    :return: A boolean
    """
    upperValue = value.upper()
    reverseStr = upperValue[::-1]
    newReverse = ''
    newUpper = ''
    for i in reverseStr:
      if i != ' ':
        newReverse += i
    for i in upperValue:
      if i != ' ':
        newUpper += i
    if newUpper == newReverse:
        return True
    else:
        return False  # remove pass statement and 
print(is_palindrome('Do geese see God'))