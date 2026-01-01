from HelperFunctions import *
from q2 import GetShortestPath
    
def GetShortestPathGrid(grid, source, destination):
    # WRITE YOUR CODE HERE
    G={}
    nodes=[]
    edges=[]
    for x in range(len(grid)):
        for y in range(len(grid)):
            
            if grid[x][y]!=-1:
                # nodes.append((x,y))
                Connected=False
                #right
                if 0<=x+1<len(grid):
                    if grid[x+1][y]+grid[x][y]==2:
                        edges.append(((x,y),(x+1,y),1))
                        Connected=True
                #left
                if 0<=x-1<len(grid):
                    if grid[x-1][y]+grid[x][y]==2:
                        edges.append(((x,y),(x-1,y),1))
                        Connected=True
                #down
                if 0<=y+1<len(grid):
                    if grid[x][y+1]+grid[x][y+1]==2:
                        edges.append(((x,y),(x,y+1),1))
                        Connected=True
                #up    
                if 0<=y-1<len(grid):
                    if grid[x][y-1]+grid[x][y-1]==2:
                        edges.append(((x,y),(x,y-1),1))
                        Connected=True
                if Connected:
                    nodes.append((x,y))
    AddNodes(G, nodes)
    AddEdges(G, edges, directed=True)
    print(G)
    return GetShortestPath(G, source, destination)
    pass


#############################################################################
# Let's test your code... Run your code file and check manually whether the #
# code is running as expected...                                            #
#############################################################################
if __name__ == "__main__":
    grid =[[1, 1, 1], [-1, 1, 1], [1, -1, 1]]
    source = (0, 0)
    destination = (2, 2)
    print(GetShortestPathGrid(grid, source, destination))
    ''' Should print ANY ONE of the below shortest paths:
    [((0, 0), (0, 1), 1), ((0, 1), (1, 1), 1), ((1, 1), (1, 2), 1), ((1, 2), (2, 2), 1)]
    [((0, 0), (0, 1), 1), ((0, 1), (0, 2), 1), ((0, 2), (1, 2), 1), ((1, 2), (2, 2), 1)]
    '''

    grid = [[1, 1], [-1, 1]]
    source = (0, 0)
    destination = (1, 1)
    print(GetShortestPathGrid(grid, source, destination))
    ''' Should print:
    [((0, 0), (0, 1), 1), ((0, 1), (1, 1), 1)]
    '''

# Testing For all testcases 
# In order to test your function, type the following command on the terminal:
# py -m pytest tests/test_q3.py