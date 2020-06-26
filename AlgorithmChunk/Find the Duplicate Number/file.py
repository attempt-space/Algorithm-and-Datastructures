"""
Find the Duplicate Number

Solution
Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive), prove that at least one duplicate number must exist. Assume that there is only one duplicate number, find the duplicate one.

Example 1:

Input: [1,3,4,2,2]
Output: 2
"""
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        """
        has more run-time for this solution
        
        nums.sort()
        for i in range(len(nums)):
            if nums[i]== nums[i+1]:
                return nums[i]
                
        Rabbit and hare solution
        """
        if len(nums) == 2:
            return nums[0]
        
        slow = nums[0]
        fast = nums[0]
        
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
            
        fast = nums[0]
        
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
            
        return slow
            
        
