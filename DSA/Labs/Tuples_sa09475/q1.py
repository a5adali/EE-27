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

def most_frequent1(s):
    
s = "this is a whole sentence"
print(most_frequent(s))