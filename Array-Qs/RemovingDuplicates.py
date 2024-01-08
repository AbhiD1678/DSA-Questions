#Here we have to remove an array which does not contain any duplicates

#M1 with spcae complexity of O(n) and time complexity of O(n)

def removeDuplicates(arr,n):
    temp=[0]*n
    temp[0]=arr[0]
    res=1
    for i in range(1,n):
        if temp[res-1]!=arr[i]:
            temp[res]=arr[i]
            res+=1
    for i in range(1,res):
        arr[i]=temp[1]
    return res

#M2 with time complexity of O(n) and space complexity of O(1)

def remdup(arr,n):
    res=1
    for i in range(1,n):
        if arr[res-1]!=arr[i]:
            arr[res]=arr[i]
            res+=1
    return res