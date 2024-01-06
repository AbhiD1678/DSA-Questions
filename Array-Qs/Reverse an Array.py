'''
Given an array arr of size n. You need to reverse the array.

Example 1:

Input:
n = 5
arr[] = {1 1 2 2 3}
Output: 3 2 2 1 1
Example 2:

Input:
n = 2
arr[] = {4 2}
Output: 2 4
Your Task:
You just need to complete the function reverseArray() that takes arr and n as parameters and reverses arr. The driver code then prints arr.

Expected Time Complexity: O(n).
Expected Auxiliary Space: O(1).

Constraints:
1 <= n  <= 106
1 <= arri <= 106


'''

def reverseArray(arr,n):
    s=0
    e=n-1
    while s<e:
        arr[s],arr[e]=arr[e],arr[s]
        s=s+1
        e=e-1
    return arr

# M2
def reverseArray(arr,n):
    return arr.reverse()