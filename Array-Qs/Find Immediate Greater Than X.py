'''
Given an array arr[] of size N containing positive integers and an integer X. You need to find the value in the array which is greater than X and closest to it. ( if no such value exists the answer should be -1)

Example 1:

Input:
N = 5
arr[] = {4 67 13 12 15}
X = 16
Output: 67
Explanation: For a given value 16, there
is only one value 67 that greater than
it and so it is the answer.
Example 2:

Input:
N = 5
arr[] = {1 2 3 4 5}
X = 1
Output: 2
Explanation: For a given value 1, there
are 4 values greater than it 2 3 4 5.
But 2 is closest to 1 so it is the answer
Your Task:
Since this is a functional problem, you need to complete the given function immediateGreater() which takes 3 arguments(array arr, N and X) and returns the answer. The printing is done by the driver code.

Expected Time Complexity: O(N).
Expected Auxiliary Space: O(1).

Constraints:
1 <= N <= 103
1 <= arr[i], X <= 104
'''

class Solution:
    # inf has been imported in driver code
    def immediateGreater(self,arr,n,x):
        #return required ans
        closest=-1
        dif=float('inf')
        for num in arr:
            if num>x and num-x<dif:
                closest=num
                dif=num-x
        return closest        
        #code here
