from HelperFunctions import *
from q1 import *

def GetShortestPath(graph, source, destination):
    # WRITE YOUR CODE HERE
    if source == destination:
        return -1
    dist = {}
    prev = {}
    queue = []
    for v in graph.keys():
        dist[v] = float('inf')
        prev[v] = None
    dist[source] = 0
    EnQueue(queue, source, 0)
    
    while not IsEmpty(queue):
        current = DeQueue(queue)
        if current is None:
            continue   
        if current == destination:
            break    
        for neighbor, weight in graph[current]:
            new_dist = dist[current] + weight
            if new_dist < dist[neighbor]:
                dist[neighbor] = new_dist
                prev[neighbor] = current
                EnQueue(queue, neighbor, new_dist)
    if dist[destination] == float('inf'):
        return -1
    
    path = []
    current = destination
    while current != source:
        prev_node = prev[current]
        for node, weight in graph[prev_node]:
            if node == current:
                path.append((prev_node, current, weight))
                break
        current = prev_node
    return path[::-1]
    pass


#############################################################################
# Let's test your code... Run your code file and check manually whether the #
# code is running as expected...                                            #
#############################################################################
if __name__ == "__main__":
    graph = {
        'A': [('D', 2), ('E', 6), ('B', 7)], 
        'B': [('C', 3), ('A', 7)], 
        'C': [('B', 3), ('D', 2), ('G', 2)], 
        'D': [('A', 2), ('C', 2), ('F', 8)], 
        'E': [('A', 6), ('F', 9)], 
        'F': [('D', 8), ('E', 9), ('G', 4)], 
        'G': [('C', 2), ('F', 4)]
    }

    print(GetShortestPath(graph, 'A', 'G'))
    ''' Should print:
    [('A', 'D', 2), ('D', 'C', 2), ('C', 'G', 2)]
    '''

    print(GetShortestPath(graph, 'A', 'C'))
    ''' Should print:
    [('A', 'D', 2), ('D', 'C', 2)]
    '''

    print(GetShortestPath(graph, 'A', 'D'))
    ''' Should print:
    [('A', 'D', 2)]
    '''


# Testing For all testcases 
# In order to test your function, type the following command on the terminal:
# py -m pytest tests/test_q2.py