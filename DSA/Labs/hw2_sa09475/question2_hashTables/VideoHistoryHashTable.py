import math

# INSTRUCTIONS >> DO NOT MODIFY EXISTING CODE USE the FUNCTIONS MENTIONED IN THE FILE 
# YOU CAN CREATE YOUR OWN FUNCTIONS IF NEEDED

#Takes size as Input
#Returns Empty hast table of 'size'
#DO NOT MODIFY THIS CODE
def create_hashtable(size): # returns list of dictionaries
    htable=[{}]*size
    for i in range(size):
        htable[i]={"ID": None,"DATA": None}
    return htable


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2,( n//2)+1 ):
        if n % i == 0:
            return False
    return True
def next_prime(n):
    while not is_prime(n):
        n += 1
    return n
#Takes Existing hashtable, size and a bool indicating wether to increase or decrease the size
#Returns a Tuple Containing new Hash Table and its New Size (Hashtable,newsize)
def resize_hashtable(hashtable,size,increase):
    if increase:
        # If increasing, double the size and find the next prime number
        new_size = size * 2
        new_size = next_prime(new_size)
        
    else:
        # If decreasing, halve the size (but make sure it's not less than 7)
        new_size = size // 2
        if new_size <= 7:
            new_size = 7
        else:
            new_size = next_prime(new_size)
    
    # Create a new hashtable with the new size
    new_hashtable = create_hashtable(new_size)
    
    # Rehash all the existing keys and insert them into the new hashtable
    for index in range(size):
        if hashtable[index]["ID"] is not None and hashtable[index]["ID"] != "#":
            key = hashtable[index]["ID"]
            data = hashtable[index]["DATA"]
            new_index = hash_function(key, new_size)
            
            # Handle collisions during rehashing (using the collision resolver)
            while new_hashtable[new_index]["ID"] is not None and new_hashtable[new_index]["ID"] != "#":
                new_index = collision_resolver(key, new_index, new_size)
            
            new_hashtable[new_index] = {"ID": key, "DATA": data}
    
    # Return the resized hashtable and the new size
    return new_hashtable, new_size
    pass

#Takes Key and size as parameters
#Returns Original address of type(int) for the Key using the Hash Function Mentioned in the Document
def hash_function(key,size):
    ascii_sum = 0
    for char in key:
        ascii_sum += ord(char)
    
    shifted_value = ascii_sum >> 4
    hash_value=abs(shifted_value%size)
    # shifted_value = shifted_value % size
    # if shifted_value < 0:
    #     hash_value = shifted_value+size
    # else:
    #     hash_value = shifted_value 
    return hash_value
    pass


##Takes Key , OldAddress  and size as parameters
#Returns new address of type(int) for the Key using the Key Offset method Mentioned in the Document
def collision_resolver(key,oldAddress,size):
    offset = 0
    for char in key:
        offset += ord(char)
    offset = offset // size
    new_address = (offset + oldAddress) % size
    return new_address
    pass

#Takes hashtable, key, data and size and Insert key and Data into the Hash Table 
# After Insertion do check if the Hash table needs to be resized or not 
# if yes resize it by sending a call to resize_hashtable
#Returns the HashTable and its Size as a Tuple (hashtable,size)
def put(hashtable,key, data,size):
    index = hash_function(key, size)
    
    if hashtable[index]["ID"] is None or hashtable[index]["ID"] == "#":
        hashtable[index] = {"ID": key, "DATA": data}
    else:
        # Handle collision using the collision resolver
        new_index = collision_resolver(key, index, size)
        count=0
        while hashtable[new_index]["ID"] is not None :
            new_index = collision_resolver(key, new_index, size)
            
        if hashtable[new_index]["ID"] is None :
            hashtable[new_index] = {"ID": key, "DATA": data}
        

    lfv = loadFactor(hashtable, size)
    if lfv > 75:
        hashtable, size = resize_hashtable(hashtable, size, True)
    elif lfv < 30:
        hashtable, size = resize_hashtable(hashtable, size, False)
    
    return hashtable, size
    pass
  

#Takes hashtable and size as parameters 
# Returns load factor of type float   
def loadFactor(hashtable,size):
    x = 0
    
    for i in range(size):
        if hashtable[i]["ID"] is not None and hashtable[i]["ID"] != "#":
            x += 1
    
    load_factor = (x / size)*100
    return load_factor
    pass

#Takes in hash table, key, Name of the Column to be updated, 
# size of hash table, Collision Path and Operation Number as Parameters
#Searches for the key in hashtable and update the Column Name of the hashtable also updates the collision path of the key
#Returns Nothing
def Update(hashtable,key, columnName,data, size,collision_path,opNumber):
    index = hash_function(key, size)
    collision_path[opNumber] = [index]
    if hashtable[index]["ID"] == key:
        # If found, update the specified column with the new data
        hashtable[index][columnName] = data
        
        
    else:
    
        new_index = collision_resolver(key, index, size)
        collision_path[opNumber].append(new_index)
        count=0
        while hashtable[new_index]["ID"] is not None and hashtable[new_index]["ID"] != "#":
            new_index = collision_resolver(key, new_index, size)
            collision_path[opNumber].append(new_index)
            if new_index==index or count > size:
                count+=1


                break
        
        if hashtable[new_index]["ID"] == key:
            hashtable[new_index][columnName] = data

        else:
            
            print(f"Key '{key}' not found in the hashtable.")
    pass
        
# Update the Column Name of the hashtable founf at Index
#Returns Nothing
def UpdateAtIndex(hashtable,index,columnName,data):
    # Check if the index is within valid range
    if index < 0 or index >= len(hashtable):
        print(f"Index {index} is out of bounds.")
        return
    
    # Check if the specified columnName is valid
    if columnName not in ["ID", "DATA"]:
        print(f"Invalid column name '{columnName}'. Only 'ID' and 'DATA' are allowed.")
        return

    # Update the specified column at the given index
    hashtable[index][columnName] = data
    pass
    
   
#Takes hash table, key, size , Collision path and Operation Number as parameters
# Searches for the key in Hash table update the Collision path and 
#If key is found returns a Tuple Containing 'DATA' part of the Hash table and the index of the key  
# Return format -> (hashtable[index]['DATA],index)  
#If key is not Found return (None,None)
def get(hashtable,key,size,collision_path,opNumber):
    index = hash_function(key, size)
    
    # Check if the key is found at the initial index
    if hashtable[index]["ID"] == key:
        # Key found, return the data and the index
        collision_path[opNumber] = [index]
        return hashtable[index]["DATA"], index
    else:
        # Handle collision: Use the collision resolver to check other positions
        collision_path[opNumber] = [index]
        new_index = collision_resolver(key, index, size)
        collision_path[opNumber].append(new_index)
        count=1
        while hashtable[new_index]["ID"] != key  and hashtable[new_index]["ID"] is not None:
            # Key found at the new index, return the data and the new index
            new_index = collision_resolver(key, new_index, size)
            count+=1
            collision_path[opNumber].append(new_index)
        return hashtable[new_index]["DATA"], new_index
        
    pass


#Takes hashtable, key, size , Collision path and operation Number 
# Delete key and Data from the Hash Table 
# After deletion do check if the Hash table needs to be resized or not 
# if yes resize it by sending a call to resize_hashtable
#Returns the HashTable 
def delete(hashtable, key, size,collision_path,opNumber):
    index = hash_function(key, size)
    
    # Check if the key exists at the initial index
    if hashtable[index]["ID"] == key:
        # Key found, mark the slot with a tombstone
        hashtable[index]["ID"] = "#"
        hashtable[index]["DATA"] = "#"
        
        # Update the collision path for the operation
        collision_path[opNumber] = [index]
        
    else:
        # Handle collisions and check other positions using the collision resolver
        collision_path[opNumber] = [index]
        new_index = collision_resolver(key, index, size)
        collision_path[opNumber].append(new_index)
        while hashtable[new_index]["ID"] != key  and hashtable[new_index]["ID"] is not None:
            new_index = collision_resolver(key, new_index, size)
            collision_path[opNumber].append(new_index)
        
        if hashtable[new_index]["ID"] == key:
            # Key found at the new index, mark it with a tombstone
            hashtable[new_index]["ID"] = "#"
            hashtable[new_index]["DATA"] = "#"
            
            
        else:
            # Key not found after collision resolution
            print(f"Key '{key}' not found in the hashtable.")
    
    # After deletion, check if resizing is necessary based on the load factor
    lfv = loadFactor(hashtable, size)

    if lfv < 30 and size > 7:
        print("Resizing down", key,lfv)
        hashtable, size = resize_hashtable(hashtable, size, False)
    
    return hashtable
    pass