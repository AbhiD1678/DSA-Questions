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
# time complexity O(n) and space complexity O(1)

# Using recursion method

def ReverseArray2(arr,start,end):
    if start<=end:
        arr[start],arr[end]=arr[end],arr[start]
        ReverseArray2(arr,start+1,end-1)

# Using slicing method now

def ReverseArray3(arr):
    return arr[::-1]
