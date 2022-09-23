# Given an array of integers nums, calculate the pivot index of this array.

# The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right.

# If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left. This also applies to the right edge of the array.

# Return the leftmost pivot index. If no such index exists, return -1.

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
#         listlen = len(nums)
#         for pivot in range(listlen):
#             leftsum = 0
#             rightsum = 0
            
#             for i in range(0,pivot):
#                 leftsum += nums[i]
                
#             for j in range(pivot+1,listlen):
#                 rightsum += nums[j]
                
#             if leftsum == rightsum:
#                 return pivot
#         return -1
        totalsum = sum(nums)
        leftsum = 0
        for i, num in enumerate(nums):
            totalsum -= num

            if totalsum == leftsum:
                return i
            leftsum +=num
            
        return -1
        
            