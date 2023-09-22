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

/*Second approach 
Using Linear Search
*/
var MinMax=function(arr){
    let minmax={}
    minmax.min=arr[0]
    minmax.max=arr[0]
    for(let i=0;i<arr.length;i++){
        if(arr[i]<minmax.min){
            minmax.min=arr[i]
        }
        else if(arr[i]>minmax.max){
            minmax.max=arr[i]

        }
    }
    return minmax
}

/*Third Approach,the best one with time complexity of o(n) */
var MinMax=function(arr){
let n = arr.length
let mx,mn,i
 
// If array has even number of elements then
// initialize the first two elements as minimum
// and maximum
if(n % 2 == 0){
    mx = Math.max(arr[0], arr[1])
    mn = Math.min(arr[0], arr[1])
     
    // set the starting index for loop
    i = 2
}
     
// If array has odd number of elements then
// initialize the first element as minimum
// and maximum
else{
    mx = mn = arr[0]
     
    // set the starting index for loop
    i = 1
}
     
// In the while loop, pick elements in pair and
// compare the pair with max and min so far
while(i < n - 1){
    if(arr[i] < arr[i + 1]){
        mx = Math.max(mx, arr[i + 1])
        mn = Math.min(mn, arr[i])
    }
    else{
        mx = Math.max(mx, arr[i])
        mn = Math.min(mn, arr[i + 1])
    }
         
    // Increment the index by 2 as two
    // elements are processed in loop
    i += 2
}
 
return [mx, mn]
}