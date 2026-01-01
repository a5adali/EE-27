from Q1 import *


def get_warehouse_connections(graph, wh, option):
    """
    Retrieves a list of connected warehouses based on the given option.

    This function finds all the warehouses that are directly connected to or from 
    the given warehouse in the supply chain graph.

    Parameters:
    graph (dict): The supply chain graph created in Q1, represented as an adjacency map.
    wh (str): The alphanumeric warehouse ID for which connections are being retrieved.
    option (str): A character indicating the type of connections to retrieve:
        - "o" for outbound supply (warehouses receiving shipments from `wh`).
        - "i" for inbound supply (warehouses sending shipments to `wh`).
        - "b" for both inbound and outbound connections (for repeating values, keep only a single reference).

    Returns:
    list: A list of unique warehouse IDs that are connected to the given warehouse.
          If there are no connections, the function returns an empty list.

    Example:
    >>> get_warehouse_connections(G, "W1", 'o')
    (Warehouse, W1 exists so get its outbound connections in a list and return the list)
    ['W11', 'W4']

    >>> get_warehouse_connections(G, "W1", 'i')
    (Warehouse, W1 exists so get its inbound connections in a list and return the list)
    ['W11', 'W14', 'W5']

    >>> get_warehouse_connections(G, "W1", 'b')
    (Warehouse, W1 exists so get both its inbound and outbound links without repeated values in a list and return the list)
    ['W11', 'W4', 'W14', 'W5']

    >>> get_warehouse_connections(G, "W24", 'b')
    (Warehouse, W24 does not exist so no need to check for its connections, and return an empty list)
    []
    """
    if option == "o":  #outbound connections
        result = []
        #find the outbound edges for the specified warehouse
        for key in graph:
            if key[0] == wh:
                #extract destinations and avoid duplicates
                for destination in graph[key]:
                    dest_wh = destination[0]
                    if dest_wh not in result:
                        result.append(dest_wh)
                break  #found the warehouse, no need to continue
        return result
    elif option == "i":  #inbound connections
        result = []
        #check all warehouses to find those that connect to wh
        for source_key in graph:
            destinations = graph[source_key]
            #check if any destination is our target warehouse
            for dest in destinations:
                if dest[0] == wh and source_key[0] not in result:
                    result.append(source_key[0])
                    break
        return result
    
    elif option == "b":  #both inbound and outbound
        #Get outbound connections first
        outbound = []
        for key in graph:
            if key[0] == wh:
                for destination in graph[key]:
                    dest_wh = destination[0]
                    if dest_wh not in outbound:
                        outbound.append(dest_wh)
                break
        #then get inbound connections
        inbound = []
        for source_key in graph:
            has_connection = False
            for dest in graph[source_key]:
                if dest[0] == wh:
                    has_connection = True
                    break
            if has_connection and source_key[0] not in inbound:
                inbound.append(source_key[0])
        
        #combine both lists avoiding duplicates
        combined = outbound.copy()  #start with outbound connections
        for wh_in in inbound:
            if wh_in not in combined:
                combined.append(wh_in)
                
        return combined
    
    return []  #default empty list for invalid options

    pass


def get_number_of_warehouse_connections(graph, wh, option):
    """
    Computes the number of unique warehouse connections based on the given option.

    This function finds the total number of unique warehouses connected to or from 
    the given warehouse in the supply chain graph.

    Parameters:
    graph (dict): The supply chain graph created in Q1, represented as an adjacency map.
    wh (str): The alphanumeric warehouse ID for which the number of connections is being calculated.
    option (str): A character indicating the type of connections to count:
        - "o" for outbound supply (warehouses receiving shipments from `wh`).
        - "i" for inbound supply (warehouses sending shipments to `wh`).
        - "b" for both inbound and outbound connections (for repeating values, keep only a single reference).

    Returns:
    int: The number of unique warehouses connected to the given warehouse.
         If there are no connections or the warehouse does not exist, the function returns 0.
    """

    # provide implementation here
    return len(get_warehouse_connections(graph, wh, option))
    pass


def main():
    G = create_supply_chain('supply_chain.csv')
    f = get_warehouse_connections(G, "W1", 'o')
    print(f)

    """
    EXPECTED OUTPUT:
    ['W11', 'W4']
    """

    f = get_warehouse_connections(G, "W1", 'i')
    print(f)

    """
    EXPECTED OUTPUT:
    ['W11', 'W14', 'W5']
    """
    
    f = get_warehouse_connections(G, "W1", 'b')
    print(f)

    """
    EXPECTED OUTPUT:
    ['W11', 'W4', 'W14', 'W5']
    """

    f = get_warehouse_connections(G, "W24", 'o')
    print(f)

    """
    EXPECTED OUTPUT:
    []
    """

    f = get_warehouse_connections(G, "W24", 'i')
    print(f)

    """
    EXPECTED OUTPUT:
    []
    """
    
    f = get_warehouse_connections(G, "W24", 'b')
    print(f)

    """
    EXPECTED OUTPUT:
    []
    """

    l = get_number_of_warehouse_connections(G, "W1", 'b')
    print(l)

    """
    EXPECTED OUTPUT:
    4
    """

    l = get_number_of_warehouse_connections(G, "W24", 'b')
    print(l)
    
    """
    EXPECTED OUTPUT:
    0
    """


if __name__ == "__main__":
    main()
