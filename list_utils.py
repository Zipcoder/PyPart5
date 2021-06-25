from typing import List
from math import ceil


def get_item_at_position(list_in: List, pos: int) -> List:
    """
    Returns the item at pos.

    :param list_in: Input list
    :param pos: Position of desired item in list_in
    :return: Item in pos
    """
    return list_in[pos]  # remove pass statement and implement me


def print_list_items(list_in: List) -> None:
    """
    Given a list, this function iterates through it and prints each element.

    :param list_in: Input list
    :return: None
    """
    for i in list_in:
        print(i)  # remove pass statement and implement me


def sort_by_commit_count(list_in: List) -> List:
    """
    Given a list of entries, return a new list sorted based on the commit count.

    :param list_in: A list where each entry is a list containing a name and the commit count corresponding to a user
    :return: The same list sorted in ascending order based on the commit count
    """
    list_in.sort(key = lambda x: x[1])
    return list_in

print(sort_by_commit_count([['john', 15],
     ['jane', 12],
     ['dave', 10]]))
    
    


def gen_list_of_nums(n: int) -> List[int]:
    """
    Given a number (N), this function returns a list of integers from 0 to N (exclusive).

    :param n: The number of items the result should contain
    :return: A list of integers
    """
    newList = []
    for i in range(n):
        newList.append(i)
    return newList  # remove pass statement and implement me


def half_list(list_in: List, half: int) -> List:
    """
    Given a list, this function will return a new list that contains half of the items in the list_in parameter.

    :param list_in: The list which will be used to generate the return value
    :param half: 1 will use the first half of the input list. 2 will use the second half of the input list.
    If the length of list_in is an odd number, round the half value up (hint: math.ceil()).
    :return: A list.
    """
    middle = len(list_in) // 2
    print(middle)
    if half == 1:
        if len(list_in) % 2 == 0:
            return list_in[0: middle]
        else:
            return list_in[0: middle + 1]
    else:
      return list_in[middle:]

print(half_list([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 2))
    
          # remove pass statement and implement me


def remove_odds(list_in: List[int]) -> None:
    """
    Given a list of integers, this function removes the odd numbers from the same list.

    :return: None
    """
    indexOfOdds = []
    for i in list_in:
        if i % 2 != 0:
            indexOfOdds.append(i)
            print(indexOfOdds)
    for i in indexOfOdds:
        list_in.remove(i)
    return list_in
    
      #remove pass statement and implement me


def remove_evens(list_in: List[int]) -> None:
    """
    Given a list of integers, this function removes the even numbers from the same list.

    :return: None
    """
    indexOfEvens = []
    for i in list_in:
        if i % 2 == 0:
            indexOfEvens.append(i)
        print(indexOfEvens)
    for i in indexOfEvens:
        list_in.remove(i)
    return list_in
     # remove pass statement and implement me


def concatenate_lists(list_a: List, list_b: List) -> List:
    """
    Given two lists, this function combines them and returns the result as a new list.

    :param list_a: A list
    :param list_b: Another list
    :return: A list containing all elements from list_a and list_b
    """
    list_c = list_a + list_b 
    return list_c # remove pass statement and implement me


def multiply_list(list_in: List, scalar: int) -> List:
    """
    Given a list and an integer, this function will return a new list which is the result of multiplying
    the input list by the value of the scalar.

    :param list_in: A list
    :param scalar: An integer
    :return: A list
    """
    new_List = list_in * scalar
    return new_List  # remove pass statement and implement me
