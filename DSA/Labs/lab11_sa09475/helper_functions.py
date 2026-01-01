import csv
import math

###########################################################################################
############################# PASTE YOUR LAB10 FUNCTIONS HERE #############################

def addNodes(G, nodes) -> None:
    for i in nodes:
        if i not in G:
            G[i]=[]
    return G
    pass


def addEdges(G, edges, directed: bool = False) -> None:
    for i in edges:
        G[i[0]].append((i[1],i[2]))
        if not directed:
            G[i[1]].append((i[0], i[2]))
    return G
    pass


def listOfNodes(G):
    lst=[]
    for i in G.keys():
        lst.append(i)
    return lst
    pass


def listOfEdges(G, directed: bool = False):
    edges=[]
    for i in G:
        for j in G[i]:
            if directed:
                edges.append((i, j[0], j[1]))
            else:
                if (j[0], i, j[1]) not in edges:
                    edges.append((i, j[0], j[1]))
    return edges
    pass


def getNeighbours(G, node):
    n=[]
    for i in G[node]:
        n.append(i[0])
    return n
    pass


def getNearestNeighbor(G, node):
    s = math.inf
    closest = math.inf
    for i in G[node]:
        if i[-1]<s:
            s = i[-1]
            closest = i[0]
    return closest
    pass


def removeNode(G, node) -> None:
    if node in G:
        del G[node]
    for i in G:
        for j in G[i]:
            if j[0]==node:
                G[i].remove(j)
    pass


def removeNodes(G, nodes) -> None:
    for i in nodes:
        removeNode(G, i)
    pass


def displayGraph(G) -> None:
    print(G)
    pass

##############################################################################################
############################# COMPLETE YOUR LAB11 FUNCTIONS HERE #############################


def in_out_degree(G):
    """In and out degree of a directed graph

    Parameters
    ----------
    G :
        A graph represented as a dictionary

    Returns
    -------
        A dictionary containing the in and out degree of each node
    """

    # WRITE YOUR CODE HERE
    dict1 = {}
    out_deg = 0
    for k in G.keys():
        in_deg = 0
        out_deg = 0
        for i in (G[k]):
            out_deg +=1
        for v in G.values():
            for j in v:
                if j[0] == k:
                    in_deg += 1
        dict1[k] = (in_deg, out_deg)
    return (dict1)
    pass


def degree(G):
    """Degree of a directed graph

    Parameters
    ----------
    G :
        A graph represented as a dictionary

    Returns
    -------
        A dictionary containing the degree of each node
    """

    # WRITE YOUR CODE HERE
    dict2={}
    for k in G.keys():
        deg = 0
        for i in G[k]:
            deg += 1
        dict2[k] = deg
    return (dict2)
    pass


def getInNeighbors(G, node):
    """In neighbors of a node in a directed graph

    Parameters
    ----------
    G :
        A graph represented as a dictionary
    node :
        The node whose in neighbors

    Returns
    -------
        A list of in neighbors of the node
    """

    # WRITE YOUR CODE HERE
    lst = []
    for k in G.keys():
        if k == node:
            for k, v in G.items():
                for j in v:
                    if j[0] == node:
                        lst.append(k)
            return(lst)
    pass


def getOutNeighbors(G, node):
    """Out neighbors of a node in a directed graph

    Parameters
    ----------
    G :
        A graph represented as a dictionary
    node :
        The node whose out neighbors

    Returns
    -------
        A list of out neighbors of the node
    """

    # WRITE YOUR CODE HERE
    lst =[]
    for k, v in G.items():
        if k == node:
            for i in v:
                lst.append(i[0])
    return(lst)
    pass


def isNeighbor(G, node1, node2):
    """Returns True if Node2 is a neighbor of Node1 in a directed graph G.

    Parameters
    ----------
    G : dict
        A directed graph as an adjacency list.
    Node1 : any
        The node to check outgoing edges from.
    Node2 : any
        The node to check as a neighbor of Node1.

    Returns
    -------
    bool
        True if there is an edge from Node1 to Node2, False otherwise.
    """

    # WRITE YOUR CODE HERE
    flag = False
    for k, v in G.items():
        if k == node1:
            for i in v:
                if i[0] == node2:
                    flag = True
                    return (flag)
    return (flag)
    pass


def initialize_matrix(rows, cols):
    """Initialize a matrix with -1

    Parameters
    ----------
    rows : int
        number of rows
    cols : int
        number of columns

    Returns
    -------
    list[list[int]]
        A matrix with -1
    """
    # WRITE YOUR CODE HERE
    arr = [[-1 for i in range(cols)] for j in range(rows)]
    return arr
    pass


def adjlst_to_adj_matrix(G):
    """Convert adjacency list to adjacency matrix

    Parameters
    ----------
    G :
        A graph represented as a dictionary

    Returns
    -------
        An adjacency matrix of the graph
    """

    # WRITE YOUR CODE HERE
    matrixx = initialize_matrix(len(listOfNodes(G)), len(listOfNodes(G)))
    x = -1
    NodesL = list(G.keys())
    for k in G.keys():
        x+=1
        for i in (G[k]):
            matrixx[x][NodesL.index(i[0])] = i[1]
    return(matrixx)
    pass


def csv_to_adj_list(filename: str):
    """Convert CSV to adjacency list

    Parameters
    ----------
    filename : str
        The name of the CSV file

    Returns
    -------
        A graph represented as a dictionary
    """

    # WRITE YOUR CODE HERE
    file = open(filename, "r")
    Nodes = file.readline()
    Nodes = Nodes.split(",")
    Nodes = Nodes[1:]
    last = Nodes[-1]
    Nodes[-1] = last[0:len(last)-1]
    n = len(Nodes)
    City_graph = initialize_matrix(n, n)
    adj_list = {}
    for r in range(n):
        lst = file.readline().split(",")
        lst = lst[1:]
        last = lst[-1]
        lst[-1] = last[0:len(last)-1]
        for c in range(n):
            City_graph[r][c] = int(lst[c])
    addNodes(adj_list, Nodes)
    for i in range(n):
        for j in range(n):
            if City_graph[i][j] != -1 and City_graph[i][j] != 0:
                adj_list[Nodes[i]].append((Nodes[j], City_graph[i][j]))
    return adj_list
    pass


#############################################################################
# Let's test your code... Run your code file and check manually whether the #
# code is running as expected...                                            #
# Visible Testcases are available in main_helper_functions.py               #
#############################################################################

if __name__ == "__main__":
    import main_helper_functions

    main_helper_functions.main()


# Testing For all testcases
# In order to test your function, type the following command on the terminal:
# pytest tests/test_helper_functions.py