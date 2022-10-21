
# Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

# Example 1:

# Input: nums = [1,2,3,1], k = 3
# Output: true

# class Solution:
#     def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
#         tempdict= {}
        
#         for index,value in enumerate(nums):
#             if value in tempdict and index - tempdict[value] <=k:
#                 return True
#             tempdict[value] = index
#         return False


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        tempdict= {}
        
        for index,value in enumerate(nums):
            if value not in tempdict:
                tempdict[value] = index
            elif index - tempdict[value] <=k:
                return True
            tempdict[value] = index
        return False
        