# Tip: Import and use created Stack functions from q1. (from q1 import *)
from q1 import *

def Infix_to_Postfix(expression):
    """
    Converts an infix expression to a postfix expression.

    Parameters:
    expression (str): The input infix expression as a string.

    Returns:
    str: The corresponding postfix expression as a string.

    Note:
        1. Only Stack ADT Operations are to be used in your implementation:
            ( Initialize() , push() , pop() , top() and is_empty() ).
        2. Use Stack ADT operations on the Stack only.
        3. Infix to Postfix Conversion Simulator: 
            https://raj457036.github.io/Simple-Tools/prefixAndPostfixConvertor.html
    """
    
    # WRITE YOUR CODE HERE
    expression = expression.split(" ")
    out = []
    st = Initialize(len(expression))
    for e in expression:
        if e.isalpha() == True:
            out.append(e)
        elif e == "+" or e == "-" or e == "*" or e == "/" or e == "(":    
            if e == "(":
                push(st, e)
            else:
                while True:
                    n = top(st)
                    if e == "+" or e == "-":
                        if n == "+" or n == "-" or n == "*" or n == "/":
                            out.append(n)
                            pop(st)
                        else:               
                            push(st, e)
                            break
                    elif e == "*" or e == "/":
                        if n == "*" or n == "/":
                            out.append(n)
                            pop(st)
                        else:                
                            push(st, e)
                            break
        else:
            while not is_empty(st):
                n = top(st)
                if n == "+" or n == "-" or n == "*" or n == "/":
                    out.append(n)
                    pop(st)
                elif (e == ")" and n == "("):
                    pop(st)
                    break
    for i in range(NumberOfElements(st)):
        out.append(pop(st))
    s = out[0]
    for i in range(1, len(out)):
        s += " " + out[i]
    return s
    pass


#############################################################################
# Let's test your code on visible test cases... Run your code file and      #
# check manually whether the code is running as expected...                 #
#############################################################################
if __name__ == "__main__":
    print(Infix_to_Postfix("( A + B ) * ( C + D )"))
    # Should print "A B + C D + *"

    print(Infix_to_Postfix("A * B + C * D"))
    # Should print "A B * C D * +"

    print(Infix_to_Postfix("A * B + C"))
    # Should print "A B * C +"

    print(Infix_to_Postfix("A * ( B + C )"))
    # Should print "A B C + *"

    print(Infix_to_Postfix("( A + B ) * C - ( D - E ) * ( F + G )"))
    # Should print "A B + C * D E - F G + * -"

    print(Infix_to_Postfix("( ( ( A + B ) * C ) - ( ( D - E ) * ( F + G ) ) )"))
    # Should print: "A B + C * D E - F G + * -"

    print(Infix_to_Postfix("( P + Q ) * ( M - N )"))
    # Should print: "P Q + M N - *"

    ##################################################################
    # YOU CAN DO FURTHER CUSTOM TESTING BELOW ....                   #
    ##################################################################




# Testing For all testcases 
# In order to test your function, type the following command on the terminal:
# pytest test_q5.py