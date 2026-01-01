def quick_sort_rectangles(rectangle_records, low, high, column):
    """
    Sorts a list of rectangle records in-place by the specified key using QuickSort.
    Uses the lowest index as the pivot for partitioning.
    
    Parameters:
    rectangle_records (list of dict): Rectangle records to sort.
    low (int): Starting index.
    high (int): Ending index.
    record_title (str): Key to sort by ("ID", "Length", "Breadth", or "Color").
    
    Returns:
    None
    """

    # WRITE YOUR CODE HERE
    if low < high:
        pi = partition_mid(rectangle_records, low, high, column)
        print(rectangle_records)
        quick_sort_rectangles(rectangle_records, low, pi - 1, column)
        quick_sort_rectangles(rectangle_records, pi + 1, high, column)
    pass



def partition(rectangle_records, low, high, column):
    pi = low
    i = low + 1

    for j in range(low + 1, high + 1):
        if rectangle_records[j][column] <= rectangle_records[pi][column]:
            rectangle_records[i], rectangle_records[j] = rectangle_records[j], rectangle_records[i]
            i += 1
    rectangle_records[pi], rectangle_records[i - 1] = rectangle_records[i - 1], rectangle_records[pi]
    pi = i - 1  
    return pi

def partition_mid(rectangle_records, low, high, column):
    pi = low
    rectangle_records[low], rectangle_records[pi] = rectangle_records[pi], rectangle_records[low]
    return partition(rectangle_records, low, high, column)

#############################################################################
# Let's test your code on visible test cases... Run your code file and      #
# check manually whether the code is running as expected...                 #
#############################################################################
if __name__ == "__main__":
    quick_sort_rectangles(
        [
            {"ID": "Rect1", "Length": 40, "Breadth": 25, "Color": "red"},
            {"ID": "Rect2", "Length": 30, "Breadth": 20, "Color": "blue"},
            {"ID": "Rect3", "Length": 70, "Breadth": 45, "Color": "green"},
            {"ID": "Rect4", "Length": 20, "Breadth": 10, "Color": "purple"}
        ], 0, 3, "Length")
    ''' Should print:
        [
            {'ID': 'Rect4', 'Length': 20, 'Breadth': 10, 'Color': 'purple'},
            {'ID': 'Rect2', 'Length': 30, 'Breadth': 20, 'Color': 'blue'},
            {'ID': 'Rect1', 'Length': 40, 'Breadth': 25, 'Color': 'red'},
            {'ID': 'Rect3', 'Length': 70, 'Breadth': 45, 'Color': 'green'}
        ]

        [
            {'ID': 'Rect4', 'Length': 20, 'Breadth': 10, 'Color': 'purple'},
            {'ID': 'Rect2', 'Length': 30, 'Breadth': 20, 'Color': 'blue'},
            {'ID': 'Rect1', 'Length': 40, 'Breadth': 25, 'Color': 'red'},
            {'ID': 'Rect3', 'Length': 70, 'Breadth': 45, 'Color': 'green'}
        ]
    '''

    print()

    quick_sort_rectangles(
        [
            {"ID": "Rect1", "Length": 40, "Breadth": 25, "Color": "red"},
            {"ID": "Rect2", "Length": 30, "Breadth": 20, "Color": "blue"},
            {"ID": "Rect3", "Length": 70, "Breadth": 45, "Color": "green"},
            {"ID": "Rect4", "Length": 20, "Breadth": 10, "Color": "purple"}
        ], 0, 3, "ID")
    ''' Should print:
        [
            {'ID': 'Rect1', 'Length': 40, 'Breadth': 25, 'Color': 'red'},
            {'ID': 'Rect2', 'Length': 30, 'Breadth': 20, 'Color': 'blue'},
            {'ID': 'Rect3', 'Length': 70, 'Breadth': 45, 'Color': 'green'},
            {'ID': 'Rect4', 'Length': 20, 'Breadth': 10, 'Color': 'purple'}
        ]

        [
            {'ID': 'Rect1', 'Length': 40, 'Breadth': 25, 'Color': 'red'},
            {'ID': 'Rect2', 'Length': 30, 'Breadth': 20, 'Color': 'blue'},
            {'ID': 'Rect3', 'Length': 70, 'Breadth': 45, 'Color': 'green'},
            {'ID': 'Rect4', 'Length': 20, 'Breadth': 10, 'Color': 'purple'}
        ]

        [
            {'ID': 'Rect1', 'Length': 40, 'Breadth': 25, 'Color': 'red'},
            {'ID': 'Rect2', 'Length': 30, 'Breadth': 20, 'Color': 'blue'},
            {'ID': 'Rect3', 'Length': 70, 'Breadth': 45, 'Color': 'green'},
            {'ID': 'Rect4', 'Length': 20, 'Breadth': 10, 'Color': 'purple'}
        ]
    '''

    ##################################################################
    # YOU CAN DO FURTHER CUSTOM TESTING BELOW ....                   #
    ##################################################################


    

# Testing For all testcases 
# In order to test your function, type the following command on the terminal:
# pytest test_q3.py