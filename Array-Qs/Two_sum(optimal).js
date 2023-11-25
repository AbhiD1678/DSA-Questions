/*1. Two Sum
Easy
50.8K
1.6K
Companies
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
 

Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.
 
*/

var two_sum=function TwoSum(nums,target){
    let numbertomap=[]
    for(let p = 0; p<nums.length;p++){
        let constNumber=numbertomap[nums[p]] //here we are finding number in the hash table so we are appending target value 9 in hash table,so here we are finding nums[p] and not target_value
        if(constNumber>=0){
            return [constNumber,p]
        }
        else{
            let value_target=target-nums[p]
            numbertomap[value_target]=p
        }

    }
    return []

}
/*
Dry run for first method
numbertomap={} when 2 is given then 
numbertomap[2] will be checked and its not available in numbertomap
7 is appended in the numbertomap,so numbertomap={7:0}
then when 7 is taken as the input,it is present in numbertomap so we get the output

*/

// Method 2
var TwoSum=function TwoSum(nums,target){
 let numbertomap={}
 for(let p =0;p<nums.length;p++){
  let target_value=target-nums[p]
  let constNumber=numbertomap[target_value]
  if(constNumber>=0){
    return [p,constNumber]
  else{
       numbertomap[nums[p]]=p
  }

  /*
  Dry run for first test case
  numbertomap={} when 2 is the input
  then numbertomap[7] is seen if its available or not,it is not for 2
  then numbertomap={2:0}
  when 7 is taken as the input,numbertomap[2] is present and we get the output
  
  */
