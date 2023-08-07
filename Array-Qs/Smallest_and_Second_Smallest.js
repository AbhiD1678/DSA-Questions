//In this question,we have to find the smmallest and second-smallest number in an array.

//Question
/*
Given an array of integers, your task is to find the smallest and second smallest element in the array. If smallest and second smallest do not exist, print -1.

Example 1:

Input :
5
2 4 3 5 6
Output :
2 3 
Explanation: 
2 and 3 are respectively the smallest 
and second smallest elements in the array.

Example 2:

Input :
6
1 2 1 3 6 7
Output :
1 2 
Explanation: 
1 and 2 are respectively the smallest 
and second smallest elements in the array.
*/

//Solution
class Solution{
    minAnd2ndMin(arr,n){
        var small=Number.MAX_VALUE //initialising both variables as the highest max value
        var sec=Number.MAX_VALUE
        for(let i=0;i<n;i++){ //looping over the array
            if(arr[i]<small){ //if arr[i]<small so sec=small and small=arr[i]
                sec=small
                small=arr[i]
            }
            else if(arr[i]<sec && small!=arr[i]){ 
                sec=arr[i]
            }
            
            
        }
        if( sec!=Number.MAX_VALUE){ //this is for checking if there are no small and second smallest element
            return [small,sec]
        }
        else{
            return [-1] //if true then it will return -1
        }
       
    }
        
    }
