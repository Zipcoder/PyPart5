def is_anagram(first_string: str, second_string: str) -> bool:
    """
    Given two strings, this functions determines if they are an anagram of one another.
    """
    if len(first_string) != len(second_string):
        return False

    counts1 = {}
    counts2 = {}

    for ch in first_string:
        if ch in counts1:
            counts1[ch] += 1
        else:
            counts1[ch] = 1

    for ch in second_string:
        if ch in counts2:
            counts2[ch] += 1   
        else:
            counts2[ch] = 1 
    
    for key, val in counts1.items():
        if key not in counts2 or counts2[key] != val:
            return False
    
    return True

