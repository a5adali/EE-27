def update_record(student_records, ID, record_title, data):
    """
    Updates a student's record based on the given ID and record title.
    
    Args:
    students_records (list): Sorted list of student records (tuples).
    ID (str): Student ID to update.
    record_title (str): The field to update ('ID', 'Email', 'Mid1', 'Mid2').
    data (str/int): New data to set for the specified field.
    
    Returns:
    str: Message indicating the result ('Record updated', 'ID cannot be updated', or 'Record not found').
    """

    # WRITE YOUR CODE HERE
    low = 0
    high = len(student_records)-1
    while low <= high:
        mid = (low + high) // 2
        if student_records[mid][0] == ID:
            if record_title == 'ID':
                return "ID cannot be updated"
            if record_title == 'Email':
                record_index = 1
            elif record_title == 'Mid1':
                record_index = 2
            elif record_title == 'Mid2':
                record_index = 3
            new_record = list(student_records[mid])
            new_record[record_index] = data
            student_records[mid] = tuple(new_record)
            return "Record updated"
        elif ID < student_records[mid][0]:
            high = mid - 1
        else:
            low = mid + 1
    return "Record not found"

    pass

#############################################################################
# Let's test your code on visible test cases... Run your code file and      #
# check manually whether the code is running as expected...                 #
#############################################################################
if __name__ == "__main__":
    student_records = [
        ('aa02822', 'ea02822', 80, 65), 
        ('ea02822', 'updated@gmail.com', 80, 65), 
        ('fa08877', 'fa08877@st.habib.edu.pk', 75, 67), 
        ('gh04588', 'gh04588@st.habib.edu.pk', 33, 50)
    ]
    print(update_record(student_records, 'randomID', 'Mid2', 50))
    # Should print: 'Record not found'
    print(student_records)
    ''' Should print: [
        ('aa02822', 'ea02822', 80, 65),
        ('ea02822', 'updated@gmail.com', 80, 65), 
        ('fa08877', 'fa08877@st.habib.edu.pk', 75, 67), 
        ('gh04588', 'gh04588@st.habib.edu.pk', 33, 50)
    ]'''

    print()

    student_records = [
        ('aa02822', 'ea02822', 80, 65), 
        ('ea02822', 'ea02822@st.habib.edu.pk', 80, 65), 
        ('fa08877', 'fa08877@st.habib.edu.pk', 66, 67), 
        ('gh04588', 'gh04588@st.habib.edu.pk', 33, 50)
    ]
    print(update_record(student_records, 'ea02822', 'Email', 'updated@gmail.com'))
    # Should print: 'Record updated'
    print(student_records)
    '''Should print: [
        ('aa02822', 'ea02822', 80, 65), 
        ('ea02822', 'updated@gmail.com', 80, 65), 
        ('fa08877', 'fa08877@st.habib.edu.pk', 66, 67), 
        ('gh04588', 'gh04588@st.habib.edu.pk', 33, 50)
    ]'''

    print()

    student_records = [
        ('aa02822', 'ea02822', 80, 65), 
        ('ea02822', 'updated@gmail.com', 80, 65), 
        ('fa08877', 'fa08877@st.habib.edu.pk', 75, 67), 
        ('gh04588', 'gh04588@st.habib.edu.pk', 33, 50)
    ]
    print(update_record(student_records, 'fa08877', 'ID', 'change01'))
    # Should print: 'ID cannot be updated'
    print(student_records)
    ''' Should print: [
        ('aa02822', 'ea02822', 80, 65), 
        ('ea02822', 'updated@gmail.com', 80, 65), 
        ('fa08877', 'fa08877@st.habib.edu.pk', 75, 67), 
        ('gh04588', 'gh04588@st.habib.edu.pk', 33, 50)
    ]'''


    ##################################################################
    # YOU CAN DO FURTHER CUSTOM TESTING BELOW ....                   #
    ##################################################################


    

# Testing For all testcases 
# In order to test your function, type the following command on the terminal:
# pytest test_q5.py