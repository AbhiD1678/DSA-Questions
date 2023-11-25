/* 
Given an array (or string), the task is to reverse the array/string.
Examples : 
 

Input  : arr[] = {1, 2, 3}
Output : arr[] = {3, 2, 1}

Input :  arr[] = {4, 5, 1, 2}
Output : arr[] = {2, 1, 5, 4}

*/

/* Normal Methods*/

// M1 ,these are using in built function
function ReverseArray(arr){
    let arr1=arr
    return arr1.reverse()
}

//M2 using swappin

const ReverseArray1=(arr,start,end)=>{
    while(start<end){
        let temp=arr[start]
        arr[start]=arr[end]
        arr[end]=temp
    
    }
    return arr
}

//M3 using recursion

function ReverseArray2(arr,start=0,end=arr.length -1 ){
    if(start<=end){
        let temp=arr[start];
        arr[start]=arr[end];
        arr[end]=temp;

    };
    return arr;
}
