"""
You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once. Find this single element that appears only once.

Follow up: Your solution should run in O(log n) time and O(1) space.

Input: nums = [1,1,2,3,3,4,4,8,8]
Output: 2
"""
    """
    left = 0
    right = len(nums) - 1
  
    while left < right:
        mid = left + (right-left) // 2
        print(mid, nums[mid])
        if nums[mid] == nums[mid+1]:
            right = mid
        elif nums[mid] == nums[mid-1]:
            left = mid + 1
        else:
            return nums[mid]
      
    return None
    """
    #Simple One
    res = nums[0]
    for i in range(1,len(nums)):
        res ^= nums[i]
    return res                
        
