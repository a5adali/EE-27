from Q4 import *

def get_cheapest_outgoing_supply_route(graph, wh):
    """
    Finds the cheapest outgoing supply route from a given warehouse.

    This function searches for all outgoing connections from the given warehouse
    and determines the route with the lowest shipment cost.

    Parameters:
    graph (dict): The supply chain graph represented as an adjacency map.
    wh (str): The alphanumeric warehouse ID of the origin warehouse.

    Returns:
    tuple: A tuple containing (origin warehouse, destination warehouse) 
           representing the cheapest outgoing supply route.
    None: If the warehouse has no outgoing supply routes or does not exist in the graph.
    """

    # WRITE YOUR CODE HERE
    outgoing_connections = get_warehouse_connections(graph, wh, "o")
    
    #return None if no connections exist
    if not outgoing_connections:
        return None
        
    minimum_cost = float('inf')
    best_route = None
    
    #iterate through each destination warehouse
    for destination in outgoing_connections:
        #convert the cost to float before comparison
        current_cost = float(get_supply_route_details(graph, wh, destination, "cost"))
        
        #update if we found a lower cost
        if current_cost < minimum_cost:
            minimum_cost = current_cost
            best_route = (wh, destination)
            
    return best_route
    pass
    
            
def get_cheapest_incoming_supply_route(graph, wh):
    """
    Finds the cheapest incoming supply route for a given warehouse.

    This function searches for all incoming connections to the given warehouse
    and determines the route with the lowest shipment cost.

    Parameters:
    graph (dict): The supply chain graph represented as an adjacency map.
    wh (str): The alphanumeric warehouse ID of the destination warehouse.

    Returns:
    tuple: A tuple containing (origin warehouse, destination warehouse) 
           representing the cheapest incoming supply route.
    None: If the warehouse has no incoming supply routes or does not exist in the graph.
    """

    # WRITE YOUR CODE HERE
    incoming_connections = get_warehouse_connections(graph, wh, "i")
    
    if not incoming_connections:
        return None
        
    lowest_cost = float('inf')
    optimal_route = None 
    for origin in incoming_connections:
        route_cost = float(get_supply_route_details(graph, origin, wh, "cost"))
        if route_cost < lowest_cost:
            lowest_cost = route_cost
            optimal_route = (origin, wh)        
    return optimal_route
    pass

def get_expensive_outgoing_supply_route(graph, wh):
    """
    Finds the most expensive outgoing supply route from a given warehouse.

    This function searches for all outgoing connections from the given warehouse
    and determines the route with the highest shipment cost.

    Parameters:
    graph (dict): The supply chain graph represented as an adjacency map.
    wh (str): The alphanumeric warehouse ID of the origin warehouse.

    Returns:
    tuple: A tuple containing (origin warehouse, destination warehouse) 
           representing the most expensive outgoing supply route.
    None: If the warehouse has no outgoing supply routes or does not exist in the graph.
    """

    # WRITE YOUR CODE HERE
    outgoing_list = get_warehouse_connections(graph, wh, "o")
    
    #return None if no connections exist
    if not outgoing_list:
        return None
        
    max_cost = float('-inf')
    costliest_route = None  
    #find the most expensive route
    for target in outgoing_list:
        #convert the cost to float before comparison
        route_cost = float(get_supply_route_details(graph, wh, target, "cost"))
        #update if we found a higher cost
        if route_cost > max_cost:
            max_cost = route_cost
            costliest_route = (wh, target)   
    return costliest_route

    pass
            
def get_expensive_incoming_supply_route(graph, wh):
    """
    Finds the most expensive incoming supply route for a given warehouse.

    This function searches for all incoming connections to the given warehouse
    and determines the route with the highest shipment cost.

    Parameters:
    graph (dict): The supply chain graph represented as an adjacency map.
    wh (str): The alphanumeric warehouse ID of the destination warehouse.

    Returns:
    tuple: A tuple containing (origin warehouse, destination warehouse) 
           representing the most expensive incoming supply route.
    None: If the warehouse has no incoming supply routes or does not exist in the graph.
    """

    # WRITE YOUR CODE HERE
    supplier_list = get_warehouse_connections(graph, wh, "i")
    
    if not supplier_list:
        return None    
    highest_cost = float('-inf')
    priciest_route = None
    for source in supplier_list:
        current_cost = float(get_supply_route_details(graph, source, wh, "cost"))
        if current_cost > highest_cost:
            highest_cost = current_cost
            priciest_route = (source, wh)        
    return priciest_route
    pass
    

def main():
    G = create_supply_chain('supply_chain.csv')
 
    route = get_cheapest_outgoing_supply_route(G, "W14")
    print(route)

    """
    Expected Output:
    ('W14', 'W17')
    """
    
    route = get_cheapest_outgoing_supply_route(G, "W24")
    print(route)

    """
    Expected Output:
    None
    """

    route = get_expensive_outgoing_supply_route(G, "W14")
    print(route)

    """
    Expected Output:
    ('W14', 'W1')
    """

    route = get_expensive_outgoing_supply_route(G, "W24")
    print(route)

    """
    Expected Output:
    None
    """

    route = get_cheapest_incoming_supply_route(G, "W14")
    print(route)

    """
    Expected Output:
    ('W16', 'W14')
    """

    route = get_cheapest_incoming_supply_route(G, "W24")
    print(route)

    """
    Expected Output:
    None
    """

    route = get_expensive_incoming_supply_route(G, "W14")
    print(route)

    """
    Expected Output:
    ('W18', 'W14')
    """

    route = get_expensive_incoming_supply_route(G, "W24")
    print(route)

    """
    Expected Output:
    None
    """

if __name__ == "__main__":
    main()
