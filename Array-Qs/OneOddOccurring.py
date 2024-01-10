'''
Given an array of positive integers. All numbers occur an even number of times except one number which occurs an odd number of times. Find the number in O(n) time & constant space.

Examples : 

Input : arr = {1, 2, 3, 2, 3, 1, 3}
Output : 3

Input : arr = {5, 7, 2, 7, 5, 2, 5}
Output : 5
'''

def getOddOccurrence(arr,arr_size):

    for i in range(0,arr_size):
        count=0

        for j in range(0,arr_size):
            if arr[i]==arr[j]:
                count+=1
        if count%2==0:
            return arr[i]
        
    return -1

#M2 using bitwise method
# Python program to find the element occurring odd number of times

def getOddOccurrence(arr):

    # Initialize result
    res = 0
    
    # Traverse the array
    for element in arr:
        # XOR with the result
        res = res ^ element
        print(res)

    return res

# Test array
arr = [ 2, 3, 5, 4, 5, 2, 4, 3, 5, 2, 4, 4, 2]

print("%d" % getOddOccurrence(arr))