'''
Given an array a[ ] of size N. The task is to check if array is sorted or not. A sorted array can either be increasingly sorted or decreasingly sorted. Also consider duplicate elements to be sorted.

Example 1:

Input:
N = 5
a[] = {1 1 2 2 3}
Output: 1
Example 2:

Input:
N = 2
a[] = {4 2}
Output: 1
Your Task:
You just need to complete the function isSorted() that takes arr and n as parameters and returns 0 if arr is unsorted and returns 1 if arr is sorted.

Expected Time Complexity: O(N).
Expected Auxiliary Space: O(1).
'''
class Solution:
    def isSorted(self,arr,n):
        #code here
        sl=sorted(arr)
        slr=sorted(arr,reverse=True)
        if sl==arr:
            return 1
        elif slr==arr:
            return 1
        else:
            return 0 
        
#M2
class Solution:
    def isSorted(self,arr,n):
        #code here
        isIncreasinglySorted, isDecreasinglySorted = False, False
        for i in range(1, n):
            if arr[i] < arr[i-1]:
                break
        else:
            isIncreasinglySorted = True
    
        for i in range(n-1, 0, -1):
            if arr[i] > arr[i-1]:
                break
        else:
            isDecreasinglySorted = True
        
        return 1 if isIncreasinglySorted or isDecreasinglySorted else 0
        

