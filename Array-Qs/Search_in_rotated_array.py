'''
There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
Example 3:

Input: nums = [1], target = 0
Output: -1
 

Constraints:

1 <= nums.length <= 5000
-104 <= nums[i] <= 104
All values of nums are unique.
nums is an ascending array that is possibly rotated.
-104 <= target <= 104
'''

## Method 1 with simple search
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)):
            if nums[i]==target:
                return i
        return -1
## Using Built in Python Methods
class Solution:
    def search(self,nums:List[int],target:int) -> int:
        if target in nums:
            return nums.index(target)
        return -1

## Using binary search method which has the time complexity of O(logn) and space complexity of O(1)
class Solution:
    def search(self,nums:List[int],target:int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            middle = left + (right - left) // 2
            print(middle)

            if nums[middle] == target: return middle

            if nums[left] <= nums[middle]:
                if nums[left] <= target < nums[middle]: 
                    right = middle - 1
                    print(f'Changing right:{right}')
                else: 
                    left = middle + 1
                    print(f'Changing left:{left}')

            
            else:
                if nums[middle] < target <= nums[right]: left = middle + 1
                else: right = middle - 1
        
        return -1