from Helper_Functions import *

def nodes_of_level(G,level):
    queue = Initialize(100)
    visited = []
    nodes = listOfNodes(G)
    s = nodes[0]
    enQueue(queue, (s, 0)) 
    visited.append((s, 0)) 

    while not IsEmpty(queue):
        node, node_level = deQueue(queue)

        if node_level == level:
            nodes_at_req_level = []
            for visited_node, visited_level in visited:
                if visited_level == level:
                    nodes_at_req_level.append(visited_node)
            return sorted(nodes_at_req_level)

        for neighbor in G[node]:
            neighbor_node, neighbor_level = neighbor[0], node_level + 1
            if (neighbor_node, neighbor_level) not in visited:
                visited.append((neighbor_node, neighbor_level))
                enQueue(queue, (neighbor_node, neighbor_level))

    return []
    pass


#############################################################################
# Let's test your code... Run your code file and check manually whether the #
# code is running as expected...                                            #
#############################################################################
if __name__ == "__main__":
    G = {
            's': [(1, 1), (2, 1)],
            1: [(3, 1), (4, 1), (5, 1)],
            2: [(6, 1)],
            3: [],
            4: [],
            5: [],
            6: [(7, 1)],
            7: []
    }

    print(sorted(nodes_of_level(G, 1)))     # SHOULD PRINT: [1, 2]

    print(sorted(nodes_of_level(G, 2)))     # SHOULD PRINT: [3, 4, 5, 6]

    print(sorted(nodes_of_level(G, 3)))     # SHOULD PRINT: [7]

    G = {
            'Dallas': [('Austin', 200), ('Denver', 780), ('Washington', 1300)],
            'Austin': [('Houston', 160), ('Chicago', 900)],
            'Washington': [('Atlanta', 600)],
            'Denver': [],
            'Atlanta': [],
            'Chicago': [],
            'Houston': []
        }
    
    print(sorted(nodes_of_level(G, 1)))     # SHOULD PRINT: ['Austin', 'Denver', 'Washington']

    print(sorted(nodes_of_level(G, 3)))     # SHOULD PRINT: ['Atlanta', 'Chicago', 'Houston']


# Testing For all testcases 
# In order to test your function, type the following command on the terminal:
# py -m pytest tests/test_q4.py