class Solution:
    def twoSum(self,number,target):
        hashmap={}
        for p in range(len(number)):
            target_value=target-number[p]
            if target_value in hashmap: #in this we are finding target value so we have to append number to the hash table
                return [p,hashmap[target_value]]
            hashmap[number[p]]=p
        return []