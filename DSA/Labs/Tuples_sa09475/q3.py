def most_frequent(s):
    xlst=[]                         #main list
    for i in range(len(s)):
        #ylst = []
        s=s.lower()
        count = s.count(s[i])       #.count() count te number of occurences in a string
        #ylst.append(s[i])
        #ylst.append(count)
        
        x=False
        for j in range(len(xlst)):
            if xlst[j][0]==s[i]:
                x=True
        if x==False:
            xlst.append((s[i], count))
        #if a not in xlst:
        #    xlst.append(a)
        
    return xlst

s = "this is a whole sentence"
print(most_frequent(s))
lst = most_frequent(s)

def sort_by_freq(lst):
    for i in range(len(lst)-1, 0, -1):
        for j in range(i):
            if lst[j][1] < lst[j+1][1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    return lst
f_lst = sort_by_freq(lst)
print(f_lst)
def sort_same_freq(f_lst):
    for i in range(len(f_lst)):
        for j in range(0, len(f_lst) - i - 1):
            if f_lst[j][1] == f_lst[j + 1][1] and f_lst[j][0] > f_lst[j + 1][0]:
                f_lst[j], f_lst[j + 1] = f_lst[j + 1], f_lst[j]
    return f_lst
        
print(sort_same_freq(f_lst))