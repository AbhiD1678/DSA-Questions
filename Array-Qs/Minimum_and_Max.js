/*
Given an array of size N. The task is to find the maximum and the minimum element of the array using the minimum number of comparisons.

Examples:

Input: arr[] = {3, 5, 4, 1, 9}
Output: Minimum element is: 1
              Maximum element is: 9

Input: arr[] = {22, 14, 8, 17, 35, 3}
Output:  Minimum element is: 3
              Maximum element is: 35
*/

/*for sorting an array in ascending in Js,we need to call sort((a,b)=>a-b) */

/*First apprach*/
var findMaxMin = function(arr){
    let minmax={}

    arr.sort((a,b)=>a-b) /*Done for sorting an array in ascending order */

    minmax.min = arr[0]
    minmax.max=arr[arr.length -1]

    return minmax
}

