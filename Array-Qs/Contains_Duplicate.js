/*
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
*/
//Method 1,here the time complexity is O(n^2) but it has the best space complexity
var ContainDuplicate=function(nums){
    if(nums.length>1){
        for(let i=0;i<nums.length;i++){
            for(let j=i+1;j<nums.length;j++){
                if(nums[i]===nums[j]){
                    return true
                }
            }

        }
        return false
}}
//Method 2 using sorting,here the time complexity is better,O(nlogn) than the previous case but not the best
var ContainsDuplicate=function(nums){
    arr1=nums.sort()
    if(arr1.length>1){
        for(let i=0;i<arr.length;i++){
            if(arr1[i]===arr[i+1]){
                return true
            }
        }
    }
    return false
}
//Method 3 using hashset or hashmap methods,where the time complexity is O(n) and space complexity is not O(1) as it needs a space of separate array
var containsDuplicate=function(nums){
    set1=new Set()
    if(nums.length===1) return false
    for(let i =1;i<nums.length;i++){
        if(set1.has(nums[i])){
            return true
        }
        set1.add(nums[i])
    }
    return false
}
//Method 4 using hash tables,O(n)
var containsDuplicate=function(nums){
    let hashmap=[]
    for(let i=0;i<nums.length;i++){
        if(hashmap(nums[i])){
            return true
        }
        hashmap(nums[i])=1
    }
    return false
}