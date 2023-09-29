'''

Given an array (or string), the task is to reverse the array/string.
Examples : 
 

Input  : arr[] = {1, 2, 3}
Output : arr[] = {3, 2, 1}

Input :  arr[] = {4, 5, 1, 2}
Output : arr[] = {2, 1, 5, 4}


'''

# In built methods

def reversearray(arr):
    return arr.reverse()

# Better method

def ReverseArray1(arr,start,end):
    while start<end:
        arr[start],arr[end]=arr[end],arr[start]
        start+=1
        end-=1
    return arr