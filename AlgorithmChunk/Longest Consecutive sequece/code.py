"""
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

 

Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
"""

class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==0:
            return 0
        s_nums = sorted(nums)
        length = len(s_nums)
        unique=[]

        unique.append(s_nums[0])
        for each in range(1,length):
            if s_nums[each] != s_nums[each-1]:
                unique.append(s_nums[each])

        count=1
        max_count=0
        new_length = len(unique)
        for each in range(new_length):
            if (each>0 and unique[each] == unique[each-1]+1):
                count+=1
            else:
                count=1
            max_count = max(max_count,count)
                
        return max_count