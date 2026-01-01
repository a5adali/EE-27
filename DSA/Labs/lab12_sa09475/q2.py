from Helper_Functions import *

def check_cycles(G,lst):
    a=lst[len(lst)-1]
    n=getNeighbors(G,a)
    for x in range(len(lst)):
        if x<len(lst)-1:
            if lst[x+1]not in getNeighbors(G, lst[x]):
                return False
    if lst[0] in n:
        return True
    return False
    pass


#############################################################################
# Let's test your code... Run your code file and check manually whether the #
# code is running as expected...                                            #
#############################################################################
if __name__ == "__main__":
    G = {
            'Dallas': [('Austin', 200), ('Denver', 780), ('Chicago', 900)], 
            'Austin': [('Dallas', 200), ('Houston', 160)], 
            'Washington': [('Dallas', 1300), ('Atlanta', 600)], 
            'Denver': [('Atlanta', 1400), ('Chicago', 1000)], 
            'Atlanta': [('Washington', 600), ('Houston', 800)], 
            'Chicago': [('Denver', 1000)], 
            'Houston': [('Atlanta', 800)]
        }
    
    print(check_cycles(G, ['Dallas','Denver','Atlanta','Washington']))  # SHOULD PRINT:     True


    G = {
            'BOS': [('JFK', 1), ('MIA', 1), ('SFO', 1)], 
            'ORD': [('MIA', 1), ('DFW', 1)], 
            'JFK': [('BOS', 1), ('SFO', 1), ('MIA', 1), ('DFW', 1)], 
            'DFW': [('ORD', 1), ('SFO', 1), ('LAX', 1)], 
            'MIA': [('DFW', 1), ('LAX', 1)], 
            'SFO': [('LAX', 1)], 'LAX': [('ORD', 1)] 
        }
    print(check_cycles(G, ['BOS', 'MIA', 'JFK']))   # SHOULD PRINT :    False
    print(check_cycles(G, ['JFK','MIA','DFW']))     # SHOULD PRINT :    False


# Testing For all testcases 
# In order to test your function, type the following command on the terminal:
# py -m pytest tests/test_q2.py