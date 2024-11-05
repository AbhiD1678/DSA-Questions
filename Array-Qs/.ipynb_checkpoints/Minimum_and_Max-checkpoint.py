'''
Same question but the soultion is in python
'''
Class Solution:
    def MinMax(self,arr):
        arr.sort()
        minmax={"min"=arr[0],"max"=arr[-1]}
        return minmax