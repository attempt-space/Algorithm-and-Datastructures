"""
Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

 

Example 1:

Input: nums = [3,2,3]
Output: [3]
Example 2:

Input: nums = [1]
Output: [1]
Example 3:

Input: nums = [1,2]
Output: [1,2]
"""

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        from collections import defaultdict

        returnDict = defaultdict(int)
        for each in nums:
            returnDict[each]+=1

        max_key= []
        print(returnDict)
        for key,value in returnDict.items():                
            if value > (len(nums)//3):
                max_key.append(key)
        return max_key