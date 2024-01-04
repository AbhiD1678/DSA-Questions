/*
Given an integer x, return true if x is a 
palindrome
, and false otherwise.

 

Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
 

Constraints:

-231 <= x <= 231 - 1
*/
// Method 1 using the logic which is same as the one used in python

var isPalindrome = function(x) {
    var rev=0;
    var temp=x;

    while (temp >0){
        const rm=temp%10;
        rev=rev*10+rm;
        temp=Math.floor(temp/10);
    }
    return x===rev
};

//M2 using the in built function of javascript
var isPalindrome = function(x) {
    return x==x.toString().split('').reverse().join('')
 }
