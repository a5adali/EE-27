from HelperFunctions import *
from q2 import GetShortestPath

def csv_to_adj_list(filename):
    file = open('connections.csv')
    Nodes = file.readline()
    Nodes = Nodes.split(",")
    Nodes = Nodes[1:]
    last = Nodes[-1]
    Nodes[-1] = last[0:len(last)-1]
    n = len(Nodes)
    City_graph = [[-1 for _ in range(n)] for _ in range(n)]
    adj_list = {}
    for r in range(n):
        lst = file.readline().split(",")
        lst = lst[1:]
        last = lst[-1]
        lst[-1] = last[0:len(last)-1]
        for c in range(n):
            City_graph[r][c] = int(lst[c])
    AddNodes(adj_list, Nodes)
    for i in range(n):
        for j in range(n):
            if City_graph[i][j] != -1 and City_graph[i][j] != 0:
                adj_list[Nodes[i]].append((Nodes[j], City_graph[i][j]))
    return adj_list

def GetShortestDistanceBetweenCities(source,destination):
    # Write your code here
    graph = csv_to_adj_list("SkeletonFiles/connections.csv")
    return GetShortestPath(graph, source, destination)


#############################################################################
# Let's test your code... Run your code file and check manually whether the #
# code is running as expected...                                            #
#############################################################################
if __name__ == "__main__":
    print(GetShortestDistanceBetweenCities("Islamabad",'Nathiagali'))   
    '''Should print:
    [('Islamabad', 'Murree', 49), ('Murree', 'Nathiagali', 36)]
    '''

    print(GetShortestDistanceBetweenCities('Islamabad', 'Naran'))
    ''' Should print: 
    [('Islamabad', 'Murree', 49), ('Murree', 'Nathiagali', 36), ('Nathiagali', 'Abbottabad', 34), 
     ('Abbottabad', 'Mansehra', 23), ('Mansehra', 'Balakot', 37), ('Balakot', 'Kaghan', 59), 
     ('Kaghan', 'Naran', 22)]
    '''
    
    print(GetShortestDistanceBetweenCities("Islamabad", "Murree"))
    ''' Should print:
    [('Islamabad', 'Murree', 49)]
    '''

# Testing For all testcases 
# In order to test your function, type the following command on the terminal:
# py -m pytest tests/test_q4.py