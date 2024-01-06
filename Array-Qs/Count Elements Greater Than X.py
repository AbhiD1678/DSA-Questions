'''
Given an unsorted array arr[] of size N containing non-negative integers. You will also be given an integer X, the task is to count the number of elements which are strictly greater than X. The given integer may or not be present in the array given.

Example 1:

Input:
N = 5
arr[] = {4 5 3 1 2}
X = 3
Output: 2
Explanation: Here X is 3. The elements
greater than X are 4 and 5.
Example 2:

Input:
N = 6
arr[] = {2 2 2 2 2 2}
X = 3
Output: 0
Explanation: Here X is 3. There are no
elements greater than X.
Yout Task:
You just have to complete the given function greaterThanX() which takes 3 arguments(array arr, N and X) and returns the count of elements greater than X. The printing is done by the driver code.

Expected Time Complexity: O(N).
Expected Auxiliary Space: O(1).

Constraints:
1 <= N <= 106
 1 <= arr[i], X <= 105  
'''
class Solution:
    def greaterThanX(self,arr,n,x):
        #return required result
        #code here
        count=0
        for num in arr:
            if num>x:
                count+=1
        return count