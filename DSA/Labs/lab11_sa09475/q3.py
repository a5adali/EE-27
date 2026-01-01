from helper_functions import *

def create_cities_graph(filename: str):
    return csv_to_adj_list("connections.csv")
    pass


def add_connection(G):
    addEdges(G,[("Balakot", "Nathiagali", 420)], directed=True)
    return G
    pass


#############################################################################
# Let's test your code... Run your code file and check manually whether the #
# code is running as expected...                                            #
#############################################################################
if __name__ == "__main__":
    
    print("GRAPH")
    G = create_cities_graph("connections.csv")

    displayGraph(G)
    '''
    SHOULD PRINT:
    {
        'Islamabad': [('Taxila', 46), ('Murree', 49)], 
        'Taxila': [('Islamabad', 46), ('Abbottabad', 74), ('Malam Jabba', 254)], 
        'Murree': [('Islamabad', 49), ('Nathiagali', 36), ('Muzaffarabad', 68)], 
        'Nathiagali': [('Murree', 36), ('Abbottabad', 34)], 
        'Abbottabad': [('Taxila', 74), ('Nathiagali', 34), ('Mansehra', 23)], 
        'Mansehra': [('Abbottabad', 23), ('Balakot', 37), ('Bisham', 113)], 
        'Balakot': [('Mansehra', 37), ('Kaghan', 59), ('Bisham', 136)], 
        'Kaghan': [('Balakot', 59), ('Naran', 22)], 
        'Naran': [('Kaghan', 22), ('Chilas', 113)], 
        'Chilas': [('Naran', 113), ('Bisham', 199), ('Gilgit', 133), ('Hunza', 306)], 
        'Bisham': [('Mansehra', 113), ('Balakot', 136), ('Chilas', 199), ('Malam Jabba', 61)], 
        'Gilgit': [('Chilas', 133), ('Hunza', 186), ('Skardu', 208)], 
        'Hunza': [('Chilas', 306), ('Gilgit', 186), ('Khunjerab Pass', 151), ('Skardu', 381)], 
        'Khunjerab Pass': [('Hunza', 151)], 
        'Malam Jabba': [('Taxila', 254), ('Bisham', 61)], 
        'Skardu': [('Gilgit', 208), ('Hunza', 381), ('Muzaffarabad', 484)], 
        'Muzaffarabad': [('Murree', 68), ('Skardu', 484)]
    }
    '''

    print("After adding Nathiagali route in Balakot")
    add_connection(G)
    displayGraph(G)
    '''
    SHOULD PRINT:
    {
        'Islamabad': [('Taxila', 46), ('Murree', 49)], 
        'Taxila': [('Islamabad', 46), ('Abbottabad', 74), ('Malam Jabba', 254)], 
        'Murree': [('Islamabad', 49), ('Nathiagali', 36), ('Muzaffarabad', 68)], 
        'Nathiagali': [('Murree', 36), ('Abbottabad', 34)], 
        'Abbottabad': [('Taxila', 74), ('Nathiagali', 34), ('Mansehra', 23)], 
        'Mansehra': [('Abbottabad', 23), ('Balakot', 37), ('Bisham', 113)], 
        'Balakot': [('Mansehra', 37), ('Kaghan', 59), ('Bisham', 136), ('Nathiagali', 420)], 
        'Kaghan': [('Balakot', 59), ('Naran', 22)], 
        'Naran': [('Kaghan', 22), ('Chilas', 113)], 
        'Chilas': [('Naran', 113), ('Bisham', 199), ('Gilgit', 133), ('Hunza', 306)], 
        'Bisham': [('Mansehra', 113), ('Balakot', 136), ('Chilas', 199), ('Malam Jabba', 61)], 
        'Gilgit': [('Chilas', 133), ('Hunza', 186), ('Skardu', 208)], 
        'Hunza': [('Chilas', 306), ('Gilgit', 186), ('Khunjerab Pass', 151), ('Skardu', 381)], 
        'Khunjerab Pass': [('Hunza', 151)], 
        'Malam Jabba': [('Taxila', 254), ('Bisham', 61)], 
        'Skardu': [('Gilgit', 208), ('Hunza', 381), ('Muzaffarabad', 484)], 
        'Muzaffarabad': [('Murree', 68), ('Skardu', 484)]
    }
    '''


# Testing For all testcases 
# In order to test your function, type the following command on the terminal:
# pytest tests/test_q3.py