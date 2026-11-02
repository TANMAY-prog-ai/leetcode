class Solution(object):
    def twoSum(self, nums, target):
        a={}
        for i in range(len(nums)):
            b= target- nums[i]
            if(b in a):
                return [a[b],i]
            a[nums[i]]=i
                
            

