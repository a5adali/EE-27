# Tip: Import and use created helper function from q1 where applicable. (from q1 import *)
from q1 import *


def Insert(lst, index, value):
    """
    Insert the given value at the specified index in the list, shifting existing elements to make room.

    Parameters:
    - list (list): The list to insert the value into.
    - index (int): The index at which to insert the value.
    - value: The value to insert into the list.

    Returns:
    str: A string indicating the result of the insertion.
        - "List is full" if the list is already full and no insertion is possible.
        - "Invalid Index" if the provided index is outside the valid range.
                * The valid index range is between 0 and NumberOfElements(list)
        - "Element inserted successfully" if the insertion is successful.
    """

    # WRITE YOUR CODE HERE
    if IsFull(lst) == True:
        return "List is full"
    if index >= Size(lst) or index < 0 or index> NumberOfElements(lst):
        return "Invalid Index"
    if Size(lst) > index >= 0 and IsFull(lst) == False:
        # Set(lst, index, value)
        
        stored_value = Get(lst, index)       #value that needs to be inserted
        for i in range(index, NumberOfElements(lst)+1):
            if i == index:
                Set(lst,i, value)
            else:
                updated_value = Get(lst, i)  #stores value
                Set(lst, i, stored_value)
                stored_value = updated_value
    return"Element inserted successfully"
    pass


#############################################################################
# Let's test your code on visible test cases... Run your code file and      #
# check manually whether the code is running as expected...                 #
#############################################################################
if __name__ == "__main__":
    lst = Initialize(3)

    print(Insert(lst, 0, "a"))  # Should print: "Element inserted successfully"
    print(lst)  # Should print: ['a', None, None]
    print()

    print(Insert(lst, 2, "b"))  # Should print: "Invalid Index"
    print(lst)  # ['a', None, None]
    print()

    print(Insert(lst, 1, "b"))  # Should print: "Element inserted successfully"
    print(lst)  # ['a', 'b', None]
    print()

    print(Insert(lst, 4, "e"))  # Should print: "Invalid Index"
    print(lst)  # Shoud print: ['a', 'b', None]
    print()

    print(Insert(lst, 2, "c"))  # Should print: "Element inserted successfully"
    print(lst)  # Should print: ['a', 'b', 'c']
    print()

    print(Insert(lst, 3, "d"))  # Should print: "List is full"
    print(lst)  # Should print: ['a', 'b', 'c']
    print()

    #####################################################################

    lst = ["a", "b", None]
    print(Insert(lst, 1, "c"))  # Should print: "Element inserted successfully"
    print(lst)  # Should print: ['a', 'c', 'b']
    print()

    #####################################################################

    lst = ["a", "b", None]
    print(Insert(lst, 0, "c"))  # Should print: "Element inserted successfully"
    print(lst)  # Should print: ['c', 'a', 'b']
    print()

    #####################################################################

    lst = ["a", "c", None, None]
    print(Insert(lst, 0, "b"))  # Should print: "Element inserted successfully"
    print(lst)  # Should print: ['b', 'a', 'c', None]
    print()

    #####################################################################

    lst = ["a", None]
    print(Insert(lst, 0, "b"))  # Should print: "Element inserted successfully"
    print(lst)  # Should print: ['b', 'a']
    print()

    ##################################################################
    # YOU CAN DO FURTHER CUSTOM TESTING BELOW ....                   #
    ##################################################################


# Testing For all testcases
# In order to test your function, type the following command on the terminal:
# pytest test_q2.py
