# Given an integer array nums, return true if there exists a triple of indices (i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k]. If no such indices exists, return false.

# Example 1:

# Input: nums = [1,2,3,4,5]
# Output: true
# Explanation: Any triplet where i < j < k is valid.

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        min_1 = math.inf
        min_2 = math.inf
        for each in nums:
            if each <= min_1:
                min_1 = each
            elif each <= min_2:
                min_2 = each
            else:
                return True
            
        return False
                