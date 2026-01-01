def binary_search_iterative_modified(lst,item):
    """
    Search for 'item' in a sorted list 'lst'.
    Return its index if found; otherwise, insert and return the index.

    Args:
        lst (list): Sorted list.
        item (int): Item to search for.

    Returns:
        int: Index of 'item' (found or inserted).
    """

    # WRITE YOUR CODE HERE

    low = 0
    high = len(lst) - 1
    while low <= high :
        mid = (low + high) // 2
        if item == lst[mid]:
            return mid
        elif item < lst[mid]:
            high = mid - 1
        else:
            low = mid + 1

    
    lst.insert(low, item)

    return low
    pass

#############################################################################
# Let's test your code on visible test cases... Run your code file and      #
# check manually whether the code is running as expected...                 #
#############################################################################
if __name__ == "__main__":
    lst = [0, 1, 2, 8, 13, 17, 19, 32, 42]
    print(binary_search_iterative_modified(lst, 8))     # Should print: 3
    print(lst)                          # Should print: [0, 1, 2, 8, 13, 17, 19, 32, 42]

    lst = [0, 1, 2, 3, 8, 13, 17, 19, 32, 42]
    print(binary_search_iterative_modified(lst, -1))    # Should print: 0
    print(lst)                          # Should print: [-1, 0, 1, 2, 3, 8, 13, 17, 19, 32, 42]

    lst = [0, 1, 2, 8, 13, 17, 19, 32, 42]
    print(binary_search_iterative_modified(lst, 13))    # Should print: 4
    print(lst)                          # Should print: [0, 1, 2, 8, 13, 17, 19, 32, 42]

    lst = [0, 1, 2, 5, 8, 13, 15, 17, 19, 20, 32, 42]
    print(binary_search_iterative_modified(lst, 14))    # Should print: 6
    print(lst)                          # Should print: [0, 1, 2, 5, 8, 13, 14, 15, 17, 19, 20, 32, 42]

    lst = [0, 1, 2, 8, 13, 17, 19, 32, 42]
    print(binary_search_iterative_modified(lst, 0))     # Should print: 0
    print(lst)                          # Should print: [0, 1, 2, 8, 13, 17, 19, 32, 42]

    lst = [0, 1, 2, 8, 13, 17, 19, 32, 42]
    print(binary_search_iterative_modified(lst, 2))     # Should print: 2
    print(lst)                          # Should print: [0, 1, 2, 8, 13, 17, 19, 32, 42]

    lst =  [0, 1, 2, 8, 13, 17, 19, 32, 42]
    print(binary_search_iterative_modified(lst, 1))     # Should print: 1
    print(lst)                          # Should print: [0, 1, 2, 8, 13, 17, 19, 32, 42]

    lst = [0, 1, 2, 8, 13, 17, 19, 32, 42]
    print(binary_search_iterative_modified(lst, 17))    # Should print: 5
    print(lst)                          # Should print: [0, 1, 2, 8, 13, 17, 19, 32, 42]

    ##################################################################
    # YOU CAN DO FURTHER CUSTOM TESTING BELOW ....                   #
    ##################################################################


    

# Testing For all testcases 
# In order to test your function, type the following command on the terminal:
# pytest test_q2.py