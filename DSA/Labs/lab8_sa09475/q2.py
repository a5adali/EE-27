def quick_sort_by_column_number(matrix, low, high, column):
    """
    Sorts a matrix in-place by the specified column using the QuickSort algorithm
    with the highest index element as the pivot.

    Parameters:
    matrix (list of lists): The matrix to sort.
    low (int): The starting index.
    high (int): The ending index.
    columnNumber (int): The column index to sort by.

    Returns:
    None
    """

    # WRITE YOUR CODE HERE
    if low < high:
        pi = partition_mid(matrix, low, high, column)
        print(matrix)
        quick_sort_by_column_number(matrix, low, pi - 1, column)
        quick_sort_by_column_number(matrix, pi + 1, high, column)
    pass



def partition(matrix, low, high, column):
    pi = low
    i = low + 1

    for j in range(low + 1, high + 1):
        if matrix[j][column] <= matrix[pi][column]:
            matrix[i], matrix[j] = matrix[j], matrix[i]
            i += 1
    matrix[pi], matrix[i - 1] = matrix[i - 1], matrix[pi]
    pi = i - 1  
    return pi

def partition_mid(matrix, low, high, column):
    pi = high
    matrix[low], matrix[pi] = matrix[pi], matrix[low]
    return partition(matrix, low, high, column)


    pass


#############################################################################
# Let's test your code on visible test cases... Run your code file and      #
# check manually whether the code is running as expected...                 #
#############################################################################
if __name__ == "__main__":
    quick_sort_by_column_number(
        [
            ['square', 'rectangle', 'triangle'], 
            ['chair', 'table', 'house'], 
            ['motor cycle', 'car', 'truck']
        ], 0, 2, 1)
    ''' Should print:
        [
            ['motor cycle', 'car', 'truck'],
            ['chair', 'table', 'house'],
            ['square', 'rectangle', 'triangle']
        ]
        
        [
            ['motor cycle', 'car', 'truck'],
            ['square', 'rectangle', 'triangle'],
            ['chair', 'table', 'house']
        ]
    '''

    print()

    quick_sort_by_column_number(
        [
            [75, 28, 12],
            [63, 37, 23],
            [84, 15, 49]
        ], 0, 2, 1)
    
    ''' Should print:
        [
            [84, 15, 49],
            [63, 37, 23],
            [75, 28, 12]
        ]
        
        [
            [84, 15, 49],
            [75, 28, 12],
            [63, 37, 23]
        ]
    '''

    print()

    quick_sort_by_column_number([['square', 'rectangle', 'triangle'], ['chair','table', 'house'], ['motor cycle', 'car', 'truck']], 0, 2, 2)

    ##################################################################
    # YOU CAN DO FURTHER CUSTOM TESTING BELOW ....                   #
    ##################################################################


    

# Testing For all testcases 
# In order to test your function, type the following command on the terminal:
# pytest test_q2.py