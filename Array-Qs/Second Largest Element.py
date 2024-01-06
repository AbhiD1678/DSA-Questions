# Naive Solution

def getSecMax(l):
    if len(l)<=1:
        return None
    lar=getMax(l)
    slar=None
    for x in l:
        if x!=lar:
            if slar==None:
                slar=x
            else:
                slar=max(slar,x)
    return slar

def getMax(l):
    res=l[0]
    for i in range(1,len(l)):
        res=max(res,l[i])
    return res

# Efficient Solution

def getSecMax(l):
    if len(l)<=1:
        return None
    lar=l[0]
    slar=None
    for x in l[1:]:
        if x>l:
            slar=lar
            lar=x
        elif x!=lar:
            if slar==None or x<slar:
                slar=x
    return slar
