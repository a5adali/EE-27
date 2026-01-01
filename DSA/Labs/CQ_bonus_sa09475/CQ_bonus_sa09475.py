def initialise(size):
    thing= {'data':[None]*size , 'len':0, 'rear_index':-1,'front_index':-1, "size":size}
    return thing

CQ=initialise(6)

def is_full(CQ):
    if CQ['len']==CQ['size']:
        return True
    else:
        return False
    
def is_empty(CQ):
    if CQ['len']== 0:
        return True
    else:
        return False

def enqueue(CQ, val):

    if not is_full(CQ):
        if (CQ['rear_index']==-1 and CQ['front_index']==-1): #resets index back to 0
            CQ['front_index']=0
        
        CQ['rear_index']=(CQ['rear_index']+1) % CQ['size'] #updates the rear index according to the valid size of the queue
        CQ['data'][CQ['rear_index']]=val #inputs the value
        CQ['len'] +=1 #updates the valid size
        return 'rear index = ' +  str(CQ['rear_index'])

    else:

        return "Circular Array is full" #Error message

def dequeue(CQ):
        if is_empty(CQ):
            print("Circular Queue is empty")
            return None, CQ['front_index']

        val = CQ['data'][CQ['front_index']] #store front value
        CQ['data'][CQ['front_index']]= None #replace front value with None

        if CQ['front_index']!= CQ['rear_index']:
            CQ['front_index'] = (CQ['front_index'] + 1) % CQ['size'] #update front index value
        
        CQ['len'] -= 1 #update the valid size

        return val, CQ['front_index']

def size(CQ):
    return CQ['len']

def first(CQ):
    val = CQ['data']['front_index']
    if val == None:
        return "Circular Array is empty", None
    return val

print(is_empty(CQ),CQ['data'])
print(enqueue(CQ,44),CQ['data'])
print(enqueue(CQ,29),CQ['data'])
print(enqueue(CQ,31),CQ['data'])
print(enqueue(CQ,16),CQ['data'])
print(enqueue(CQ,98),CQ['data'])
print(dequeue(CQ),CQ['data'])
print(dequeue(CQ),CQ['data'])
print(enqueue(CQ,9),CQ['data'])
print(enqueue(CQ,20),CQ['data'])
print(enqueue(CQ,15),CQ['data'])
print(enqueue(CQ,32),CQ['data'])
print(dequeue(CQ),CQ['data'])
print(dequeue(CQ),CQ['data'])
print(dequeue(CQ),CQ['data'])
print(dequeue(CQ),CQ['data'])
print(dequeue(CQ),CQ['data'])
print(dequeue(CQ),CQ['data'])
print(dequeue(CQ),CQ['data'])
print(enqueue(CQ,32),CQ['data'])
print(enqueue(CQ,64),CQ['data'])