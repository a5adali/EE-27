def IsEmpty(queue):
    return queue == []

def EnQueue(queue, item, priority):
    count = 0
    for i, _ in queue:
        if i == item:
            queue[count] = item, priority
            return None
        count += 1
    queue.append((item, priority))


def DeQueue(queue):
    # WRITE YOUR CODE HERE
    minimum=100000
    deleted=-1
    for i in range(len(queue)):
        if queue[i][1]<minimum:
            minimum=queue[i][1]
            deleted=i
    if deleted==-1:
        return None
    else:
        x=queue[deleted][0]
        queue.pop(deleted)
    # queue[0]=None
   
        return x
    pass


#############################################################################
# Let's test your code... Run your code file and check manually whether the #
# code is running as expected...                                            #
#############################################################################
if __name__ == "__main__":
    queue = []
    EnQueue(queue,'A',1)
    EnQueue(queue,'B',2)
    EnQueue(queue,'C',3)
    EnQueue(queue,'D',4)
    EnQueue(queue,'E',5)
    EnQueue(queue,'F',6)
    EnQueue(queue,'G',7)
    print(queue)            # Should print: [('A', 1), ('B', 2), ('C', 3), ('D', 4), ('E', 5), ('F', 6), ('G', 7)]
    print(DeQueue(queue))   # Should print: A
    print(queue)            # Should print: [('B', 2), ('C', 3), ('D', 4), ('E', 5), ('F', 6), ('G', 7)]
    print(DeQueue(queue))   # Should print: B
    print(queue)            # Should print: [('C', 3), ('D', 4), ('E', 5), ('F', 6), ('G', 7)]

    print('-------------------------------------------------------------------')

    queue = []
    EnQueue(queue, 'A', 10)
    EnQueue(queue, 'B', 2)
    EnQueue(queue, 'C', 5)
    
    print(queue)            # Should print: [('A', 10), ('B', 2), ('C', 5)]
    print(DeQueue(queue))   # Should print: B
    print(queue)            # Should print: [('A', 10), ('C', 5)]
    print(DeQueue(queue))   # Should print: C
    print(queue)            # Should print: [('A', 10)]

# Testing For all testcases 
# In order to test your function, type the following command on the terminal:
# py -m pytest tests/test_q1.py