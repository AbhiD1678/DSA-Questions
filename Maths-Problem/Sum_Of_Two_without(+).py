'''
Sum of Two Integers
Given two integers a and b, return the sum of the two integers without using the operators + and -.

 

Example 1:

Input: a = 1, b = 2
Output: 3
Example 2:

Input: a = 2, b = 3
Output: 5
'''
class Solution:
    def getSum(self,a,b):
        return log(exp(a)*exp(b)) if a!=0 and b!=0 else a or b