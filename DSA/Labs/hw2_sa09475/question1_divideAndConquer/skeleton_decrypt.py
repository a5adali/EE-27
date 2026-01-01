# Decrypt the data using the logic of the Karatsuba algorithm.
# Args:
#   data: List of list consisting of leaves
# Returns:
#   A tuple containing the original two numbers.
def reverse_karatsuba(data, level=0) -> tuple:
    # print(f"Level {level}: {data}")

    
    for i in range(len(data)):
        if isinstance(data[i], list):
            notall=False
            break
        else:
            notall=True
    # Base case: all items are tuples
    if notall:

        L = real_L([l for l, w, h in data])
        W = real_W([w for l, w, h in data])

        H = max(h for l, w, h in data)
        if level == 0:
            H=10**H
        else:
            H = H * 10 ** (level + 1)
        return (L, W, H)

    # Mixed case: some are tuples, some are lists
    else:
        #making all tuples
        for i in range(len(data)):
            
            # print(f"Item: {data[i]}")
            while isinstance(data[i], list):
                data[i] =reverse_karatsuba(data[i], level + 1)
        
        # print(f"Combined: {data}")
        L = real_L([l for l, w, h in data])
        W = real_W([w for l, w, h in data])
        H = max(h for l, w, h in data)
        return (L, W, H)

    

def real_L(l):
    l0 = l[0]
    l1 = l[2]
    m = min(len(str(l0)), len(str(l1)))
    B = 10
    return l1 * (B ** m) + l0

def real_W(w):
    w0 = w[0]   # from z0 = l0 * w0
    # print(f"w0: {w0}")
    w1 = w[2]   # from z2 = l1 * w1
    # print(f"w1: {w1}")
    B = 10
    m = min(len(str(w0)), len(str(w1)))  
    # print(f"m: {m}")
    w = w1 * (B ** m) + w0
    # print(f"w: {w}")
    # print('-------')
    return w

# This function reads data from a specified file and decrypt data using the logic of the Karatsuba algorithm.
# Args:
#   filename: The name of the file containing input data.
# Returns:
#   A list of tuples, each tuple representing coordinates (l, w).
def main(filename) -> list[tuple[int, int]]:
    result = []

    with open("input_decrypt.txt") as f:
        lines = f.readlines()
        # print (lines)

    # input_data = []
    # for line in lines[1:]:  # skip the first line (tree count)
    #     line = line.strip()
    #     if line:
            
    #         input_data.append(eval(line))

    
    # print(input_data[1])
    # for tree in input_data:
    #     print(tree)
    input = []
    line = lines[0].strip() # remove leading and trailing spaces
    tokens = line.split() # split the line into tokens
    l= (int(tokens[0])) # add the first token to the
    # print(l)
    for i in range(l):
        line = lines[i+1].strip()
        # print(line)
        input.append(eval(line))
    
        # print(line)
    for i in range(l):
        # print(input[i])
        length, width, height = reverse_karatsuba(input[i],0)
        result.append(((length, width,height),length*width*height))  

    return result
    
    
output = main('E:\\hw2_st-master (1)\\hw2_st-master\\question1_divideAndConquer\\input_decrypt.txt')
for item in output:
    print(item)
# [(1, 3, 30), [(3, 6, 3), (7, 8, 3), (4, 2, 3)], [(2, 3, 3), (6, 5, 3), (4, 2, 3)]]
# [[(2, 1, 1), (6, 10, 1), (4, 9, 1)], [(2, 8, 1), (6, 20, 1), (4, 12, 1)], (0, 37, 10)]
