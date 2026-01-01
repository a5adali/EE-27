# Tip: Import and use created helper function from q1 where applicable. (from q1 import *)
from q1 import *


def Remove(lst, index):
    """
    Remove the element at the specified index in the list, shifting subsequent elements to fill the gap.

    Parameters:
    - list (list): The list from which to remove an element.
    - index (int): The index of the element to be removed.

    Returns:
    str: A string indicating the result of the removal.
         - "List is empty" if the list is empty, and no removal is possible.
         - "Invalid Index" if the provided index is outside the valid range.
                * The valid index range is between 0 and NumberOfElements(list)-1
         - "Element removed successfully" if the removal is successful.
    """

    # WRITE YOUR CODE HERE
    if IsEmpty(lst) == True:
        return "List is empty"
    elif index >= Size(lst) or index < 0 or index >= NumberOfElements(lst):
        return "Invalid Index"
    elif Size(lst) > index >= 0 and IsEmpty(lst) == False:
        for i in range(index, NumberOfElements(lst)):
            if i == NumberOfElements(lst)-1: 
                Set(lst, i, None) #replaces the value we need to remove with none.
            else:
                Set(lst, i, Get(lst, i+1))  #replaces the none value with the next value.
            
        return "Element removed successfully"
    pass


#############################################################################
# Let's test your code on visible test cases... Run your code file and      #
# check manually whether the code is running as expected...                 #
#############################################################################
if __name__ == "__main__":
    lst = [10, 20, 30, 40, 50]
    print(Remove(lst, 2))  # Should print: "Element removed successfully"
    print(lst)  # Should print: [10, 20, 40, 50, None]

    print(Remove(lst, 0))  # Should print: "Element removed successfully"
    print(lst)  # Should print: [20, 40, 50, None, None]
    print()

    print(Remove(lst, 5))  # Should print: "Invalid Index"
    print(lst)  # Should print: [20, 40, 50, None, None]
    print()

    print(Remove(lst, 3))  # Should print: "Invalid Index"
    print(lst)  # Should print: [20, 40, 50, None, None]
    print()

    print(Remove(lst, 4))  # Should print: "Invalid Index"
    print(lst)  # Should print: [20, 40, 50, None, None]
    print()

    ###########################################################################

    lst = Initialize(4)
    print(Remove(lst, 0))  # Should print: "List is empty"
    print(lst)  # Should print: [None, None, None, None]
    print()

    ###########################################################################

    lst = ["a", "b"]
    print(Remove(lst, 0))  # Should print: "Element removed successfully"
    print(lst)  # Should print: ['b', None]
    print()

    ###########################################################################

    lst = ["a"]
    print(Remove(lst, 0))  # Should print: "Element removed successfully"
    print(lst)  # Should print: [None]

    ##################################################################
    # YOU CAN DO FURTHER CUSTOM TESTING BELOW ....                   #
    ##################################################################


# Testing For all testcases
# In order to test your function, type the following command on the terminal:
# pytest test_q3.py
