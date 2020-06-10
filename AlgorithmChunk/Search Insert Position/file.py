"""
Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

Example 1:

Input: [1,3,5,6], 5
Output: 2
"""

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        lengthoflist = len(nums)
        if target < nums[0]:
            return 0
        for n in range(lengthoflist):
            if nums[n] == target:
                return n
            elif nums[n] < target:
                if n+1 == lengthoflist or nums[n+1] > target:
                    return n+1
        return n+1
        
