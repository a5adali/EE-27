from helper_functions import *

def create_directed_graph():
    G = {}
    Nodes = [1,2,3,4]
    Edges = [(1,2,1), (2,4,1), (3,1,1),(3,2,1), (4,3,1), (4,4,1)]
    addNodes(G, Nodes)
    addEdges(G, Edges, directed= True)
    return G
    pass


def print_graph(G):
    print(displayGraph(G))
    pass


def in_neighbors(G):
    in_neighbors_dict = {}
    for node in G:
        in_neighbors_dict[node] = []
    for node in G:
        for neighbor, _ in G[node]:
            if neighbor not in in_neighbors_dict:
                in_neighbors_dict[neighbor] = []
            in_neighbors_dict[neighbor].append(node)
    return in_neighbors_dict
    pass


def out_neighbors(G):
    out_neighbors_dict = {}
    for node in G:
        out_neighbors_dict[node] = []
    for node in G:
        neighbors = G[node]
        for neighbor, _ in neighbors:
            out_neighbors_dict[node].append(neighbor)
    return out_neighbors_dict
    pass


def generate_adjacency_matrix(G):
    return adjlst_to_adj_matrix(G)
    pass


def check_degree_sums(G):
    total_out_degree = 0
    total_in_degree = 0
    total_edges = 0

    for node in G:
        total_out_degree += len(G[node])
        total_edges += len(G[node])

    for node in G:
        for neighbor, _ in G[node]:
            total_in_degree += 1
    return total_in_degree == total_out_degree == total_edges
    pass


#############################################################################
# Let's test your code... Run your code file and check manually whether the #
# code is running as expected...                                            #
#############################################################################
if __name__ == "__main__":
    print("GRAPH")
    G = create_directed_graph()

    print_graph(G)
    '''
    SHOULD PRINT:
    {1: [(2, 1)], 2: [(4, 1)], 3: [(1, 1), (2, 1)], 4: [(3, 1), (4, 1)]}
    '''

    print("IN NEIGHBORS")
    print(in_neighbors(G))
    '''
    SHOULD PRINT:
    { 1: [3], 2: [1, 3], 3: [4], 4: [2, 4] }
    '''
    
    print("OUT NEIGHBORS")
    print(out_neighbors(G))
    '''
    SHOULD PRINT:
    { 1: [2], 2: [4], 3: [1, 2], 4: [3, 4] }
    '''

    print("ADJACENCY MATRIX")
    print(generate_adjacency_matrix(G))
    '''
    SHOULD PRINT:
    [[-1, 1, -1, -1], [-1, -1, -1, 1], [1, 1, -1, -1], [-1, -1, 1, 1]]
    '''

    print("Sum of the in-degrees of all nodes, "
    "the sum of the out-degrees of all nodes "
    "and the total number of edges are all equal: ")
    
    print(check_degree_sums(G))
    '''
    SHOULD PRINT:
    True
    '''

# Testing For all testcases 
# In order to test your function, type the following command on the terminal:
# pytest tests/test_q1.py