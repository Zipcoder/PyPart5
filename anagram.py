def is_anagram(first_string: str, second_string: str) -> bool:
    """
    Given two strings, this functions determines if they are an anagram of one another.
    """
    first1 = []
    second1 = []
    for i in first_string:
        first1.append(i)
        print('first1', first1)
    for i in second_string:
        second1.append(i)
        print('second1',second1)
        first1.sort()
        second1.sort()
    if first1 == second1:
        return True
    else:
        return False
print(is_anagram('sea', 'aes'))