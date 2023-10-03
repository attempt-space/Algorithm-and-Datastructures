class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        prefix = [0]*n
        suffix = [0]*n
        product = [0]*n
        prefix[0] =1
        for i in range(1,n):    
            prefix[i] = prefix[i-1]* nums[i-1]

        suffix[n-1] = 1
        for j in range(n-2 ,-1,-1):
            suffix[j] =suffix[j+1]*nums[j+1]
        for i in range(n):
            product[i] = prefix[i] * suffix[i]
        return product