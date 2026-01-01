# Tip: Import and use created Stack functions from q1. (from q1 import *)
from q1 import *

def balanced_braces(s):
    """
    Checks if the braces in the string are balanced using stack operations only.

    Parameters:
    s (str): The string containing braces to be checked.
    
    Returns:
    bool: True if the braces are balanced, False otherwise.

    Note:
        1. Only Stack ADT Operations are to be used in your implementation:
            ( Initialize() , push() , pop() , top() and is_empty() ).
        2. You have to use a SINGLE Stack only.
        3. You are NOT allowed to use any sort of counter to count number of brackets.
        4. You are NOT allowed to use any sort of counter to count number of opening and closing brackets.
        5. Don't use Stack ADT operations on the given string.
    """

    # WRITE YOUR CODE HERE
    stack1 = Initialize(NumberOfElements(s))
    for i in s:
        if i=="(" or i=="{" or i=="[":
            push(stack1, i)
        else:
            if i == ")" and pop(stack1) != "(":
                #if pop(stack1) != "(":
                return False
            if i == "]" and pop(stack1) != "[":
                #if pop(stack1) != "[":
                return False
            if i == "}" and pop(stack1) != "{":
                #if pop(stack1) != "{":
                return False
    if IsEmpty(stack1) == False:
        return False
    return True
    pass


#############################################################################
# Let's test your code on visible test cases... Run your code file and      #
# check manually whether the code is running as expected...                 #
#############################################################################
if __name__ == "__main__":
    print(balanced_braces("()"))                    # Should print: True

    print(balanced_braces("())"))                   # Should print: False

    print(balanced_braces("{()}"))                  # Should print: True

    print(balanced_braces("{)({"))                  # Should print: False

    print(balanced_braces("{()}[]()"))              # Should print: True

    print(balanced_braces("{[}]"))                  # Should print: False

    print(balanced_braces("()()()([{])}({{[]}})"))  # Should print: False

    ##################################################################
    # YOU CAN DO FURTHER CUSTOM TESTING BELOW ....                   #
    ##################################################################




# Testing For all testcases 
# In order to test your function, type the following command on the terminal:
# pytest test_q3.py