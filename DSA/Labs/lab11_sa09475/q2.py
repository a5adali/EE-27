from helper_functions import *
import math

def create_airport_graph():
    G = {}
    airports = ['Dallas', 'Austin', 'Washington', 'Denver', 'Atlanta', 'Chicago', 'Houston']
    flights = [('Dallas', 'Austin', 200), ('Dallas', 'Denver', 780), ('Dallas', 'Chicago', 900), ('Austin', 'Dallas', 200), ('Austin', 'Houston', 160), ('Washington', 'Dallas', 1300), ('Washington', 'Atlanta', 600), ('Denver', 'Atlanta', 1400), ('Denver', 'Chicago', 1000), ('Atlanta', 'Washington', 600), ('Atlanta', 'Houston', 800), ('Chicago', 'Denver', 1000), ('Houston', 'Atlanta', 800)]
    addNodes(G ,airports)
    addEdges(G, flights, True)
    return G
    pass


def max_inbound_outbound_airport(G) -> tuple[str, str]:
    inbound_count = {}
    outbound_count = {}
    for airport in G:
        outbound_count[airport] = len(G[airport])
        inbound_count[airport] = 0
    for airport in G:
        for neighbor, _ in G[airport]:
            inbound_count[neighbor] = inbound_count.get(neighbor, 0) + 1

    max_inbound_airport = max(inbound_count, key=inbound_count.get)
    max_outbound_airport = max(outbound_count, key=outbound_count.get)

    return max_inbound_airport, max_outbound_airport
    pass


#############################################################################
# Let's test your code... Run your code file and check manually whether the #
# code is running as expected...                                            #
#############################################################################
if __name__ == "__main__":
    print("GRAPH")
    G = create_airport_graph()

    displayGraph(G)
    '''
    SHOULD PRINT:
    {
        'Dallas': [('Austin', 200), ('Denver', 780), ('Chicago', 900)], 
        'Austin': [('Dallas', 200), ('Houston', 160)], 
        'Washington': [('Dallas', 1300), ('Atlanta', 600)], 
        'Denver': [('Atlanta', 1400), ('Chicago', 1000)], 
        'Atlanta': [('Washington', 600), ('Houston', 800)], 
        'Chicago': [('Denver', 1000)], 
        'Houston': [('Atlanta', 800)]
    }
    '''

    max_inbound, max_outbound = max_inbound_outbound_airport(G)
    print("MAXIMUM IN-BOUND:", max_inbound)     #   SHOULD PRINT: Atlanta

    print("MAXIMUM OUT-BOUND:", max_outbound)   #   SHOULD PRINT: Dallas


# Testing For all testcases 
# In order to test your function, type the following command on the terminal:
# pytest tests/test_q2.py