'''
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

 

Example 1:

Input: nums = [1,2,3,1]
Output: true
Example 2:

Input: nums = [1,2,3,4]
Output: false
Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
 

Constraints:

1 <= nums.length <= 105
-109 <= nums[i] <= 109
'''
//Method 1,using hash maps
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashmap={}
        for i in range(len(nums)-1):
                hashmap[nums[i]]=1

                if nums[i+1] in hashmap:
                    return True
        return False

//Method 2,using sorting methods
def containsDuplicate(self, nums: List[int]) -> bool:
        arr1=sorted(nums)
        for i in range(len(nums)-1):
            if arr1[i]==arr1[i+1]:
                return True
        return False

