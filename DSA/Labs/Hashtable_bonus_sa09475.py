#Helper Functions
def hash_function(key,size):
    if type(key) == str:
        sum = 0
        for c in key:
            sum += ord(c)
        key = sum
    return key%size
def collision_resolver(h1,h2, size, iteration):
    return (h1 + iteration*h2)%size
def length_of_the_ht(hash_tb):
    count = 0
    for keys in hash_tb[0]:
        if keys != -1:
            count += 1
    return count
def enqueue(pq, p, v):
    for i in range(len(pq)):
        e = pq[i]
        if e == None or e[0] > p:
            pq.insert(i, (p, v))
            break
def dequeue(pq):
    if pq[0] != None:
        item = pq[0]
        del pq[0]
        pq.append(None)
    return item
def length_of_pq(pq):
    count = 0
    for e in pq:
        if e != None:
            count += 1
    return count


# Activity One:
def NBA_teams_handling(NBA_HT, size):
    x = length_of_the_ht(NBA_HT)
    if size - x != 0:
        for _ in range(size-x):
            rank = int(input())
            name = input()
            player = (rank, name)
            key = int(input())
            h1k = hash_function(key, size)
            if NBA_HT[0][h1k] == -1:
                NBA_HT[0][h1k] = key
                NBA_HT[1][h1k] = player
            else:
                x = length_of_the_ht(NBA_HT)
                h2k = key % (size - x)
                for i in range(1, 200):
                    new_hk = collision_resolver(h1k, h2k, size, i)
                    if NBA_HT[0][new_hk] == -1:
                        NBA_HT[0][new_hk] = key
                        NBA_HT[1][new_hk] = player
                        break
#Activity Two:
def kk_hash_function(k, N):
    hk = ((k**2) + (2 * k) + 1)%N
    return hk

#Activity Three:
def ob_hash_function(k,N):
    hk = ((4*k + 20)*13) % N
    return hk

#Activity Four:
def put(ht, k, size, v, pq):
    if pq == "kk":
        i = kk_hash_function(k, size)
    elif pq == "ob":
        i = ob_hash_function(k, size)
    ht[0][i] = k
    ht[1][i] = v
def get(ht, k, size, pq):
    if pq == "kk":
        i = kk_hash_function(k, size)
    elif pq == "ob":
        i = ob_hash_function(k, size)
    v = ht[1][i]
    return v
def delitem(ht, k, size, pq):
    if pq == "kk":
        i = kk_hash_function(k, size)
        v = get(ht, k, size, "kk")
        if v != -1:
            put(ht, k, size, -1, "kk")
    elif pq == "ob":
        i = ob_hash_function(k, size)
        v = get(ht, k, size, "ob")
        if v != -1:
            put(ht, k, size, -1, "ob")
def stacking_kk(kk_pq, ht, size):
    count = 0
    while count < 10:
        key = int(input())
        item = get(ht, key, size, "kk")
        if item != -1:
            delitem(ht, key, size, "kk")
            enqueue(kk_pq, item[0], item[1])
            count += 1

#Activity Five:
def stacking_ob(ob_pq, ht, size):
    count = 0
    while count <10:
        key = int(input())
        item = get(ht, key, size, "ob")
        if item != -1:
            delitem(ht, key, size, "ob")
            enqueue(ob_pq, item[0], item[1])
            count += 1

#Activity Six and Seven:
def displaying_the_players(pq):
    extra_pq = [None for i in range(len(pq))]
    while length_of_pq(pq) > 0:
        player = dequeue(pq)
        print(player[1])
        enqueue(extra_pq, player[0], player[1])
    while length_of_pq(extra_pq) > 0:
        player = dequeue(extra_pq)
        enqueue(pq, player[0], player[1])

#Task 1
       
def main_q1(NBA_HT):
    size = len(NBA_HT[0])
    NBA_teams_handling(NBA_HT, size)
    print(NBA_HT)
    kk_pq = [None for i in range(10)]
    stacking_kk(kk_pq, NBA_HT, size)
    ob_pq = [None for i in range(10)]
    stacking_ob(ob_pq, NBA_HT, size)
    displaying_the_players(kk_pq)
    displaying_the_players(ob_pq)


#NBA_HT = ([0, -1, 52, -1, 194, -1, -1, 777, 898, 1999],[(10, "Anas"), -1, (40, "Aneeq"), -1, (50, "Rafay"), -1, -1, (20, "Musab"), (60, "Farzam"), (30, "Haris")])

# When key was zero, and zeroth index was already filled, the collision was not being handled. 
def midsquare_method(key, size): 
    value = key**2
    value = str(value)
    l = len(value)//2
    value = value[l-1] + value[l] # Taking two digits because the testing size is 25.
    value = int(value)
    return value%size
def folding_shift_method(key, size):
    key = str(key)
    r = size-1
    r = len(str(r))
    l = len(key)
    value = 0
    for i in range(0, l, r):
        value += int(key[i:i+r])
    value = int(value)%size
    return value

def NBA_teams_handling_midsquare(NBA_HT, size):
    x = length_of_the_ht(NBA_HT)
    if size - x != 0:
        for _ in range(size-x):
            rank = int(input())
            name = input()
            player = (rank, name)
            key = int(input())
            h1k = midsquare_method(key, size)
            if NBA_HT[0][h1k] == -1:
                NBA_HT[0][h1k] = key
                NBA_HT[1][h1k] = player
            else:
                x = length_of_the_ht(NBA_HT)
                h2k = key % (size - x)
                for i in range(1, 200):
                    new_hk = collision_resolver(h1k, h2k, size, i)
                    if NBA_HT[0][new_hk] == -1:
                        NBA_HT[0][new_hk] = key
                        NBA_HT[1][new_hk] = player
                        break
def NBA_teams_handling_folding_shift(NBA_HT, size):
    x = length_of_the_ht(NBA_HT)
    if size - x != 0:
        for _ in range(size-x):
            rank = int(input())
            name = input()
            player = (rank, name)
            key = int(input())
            h1k = folding_shift_method(key, size)
            if NBA_HT[0][h1k] == -1:
                NBA_HT[0][h1k] = key
                NBA_HT[1][h1k] = player
            else:
                x = length_of_the_ht(NBA_HT)
                h2k = key % (size - x)
                for i in range(1, 200):
                    new_hk = collision_resolver(h1k, h2k, size, i)
                    if NBA_HT[0][new_hk] == -1:
                        NBA_HT[0][new_hk] = key
                        NBA_HT[1][new_hk] = player
                        break

#Task 2       
def main_q2_i(NBA_HT):
    size = len(NBA_HT[0])
    NBA_teams_handling_midsquare(NBA_HT, size)
    print(NBA_HT)
    kk_pq = [None for i in range(10)]
    stacking_kk(kk_pq, NBA_HT, size)
    ob_pq = [None for i in range(10)]
    stacking_ob(ob_pq, NBA_HT, size)
    displaying_the_players(kk_pq)
    displaying_the_players(ob_pq)
def main_q2_ii(NBA_HT):
    size = len(NBA_HT[0])
    NBA_teams_handling_folding_shift(NBA_HT, size)
    print(NBA_HT)
    kk_pq = [None for i in range(10)]
    stacking_kk(kk_pq, NBA_HT, size)
    ob_pq = [None for i in range(10)]
    stacking_ob(ob_pq, NBA_HT, size)
    displaying_the_players(kk_pq)
    displaying_the_players(ob_pq)


def collision_resolver_linear(h1, size, iteration):
    return (h1 + iteration)%size
def NBA_teams_handling_linear_probing(NBA_HT, size):
    x = length_of_the_ht(NBA_HT)
    if size - x != 0:
        for _ in range(size-x):
            rank = int(input())
            name = input()
            player = (rank, name)
            key = int(input())
            h1k = hash_function(key, size)
            if NBA_HT[0][h1k] == -1:
                NBA_HT[0][h1k] = key
                NBA_HT[1][h1k] = player
            else:
                for i in range(1, 200):
                    new_hk = collision_resolver_linear(h1k, size, i)
                    if NBA_HT[0][new_hk] == -1:
                        NBA_HT[0][new_hk] = key
                        NBA_HT[1][new_hk] = player
                        break

#Task 3
def main_q3(NBA_HT):
    size = len(NBA_HT[0])
    NBA_teams_handling_linear_probing(NBA_HT, size)
    print(NBA_HT)
    kk_pq = [None for i in range(10)]
    stacking_kk(kk_pq, NBA_HT, size)
    ob_pq = [None for i in range(10)]
    stacking_ob(ob_pq, NBA_HT, size)
    displaying_the_players(kk_pq)
    displaying_the_players(ob_pq)
