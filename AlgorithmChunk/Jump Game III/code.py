class Solution:
    """
    Given an array of non-negative integers arr, you are initially positioned at start index of the array. When you are at index i, you can jump to i + arr[i] or i - arr[i], check if you can reach to any index with value 0.

    Notice that you can not jump outside of the array at any time.

    Example 1:

    Input: arr = [4,2,3,0,3,1,2], start = 5
    
    Output: true
    Explanation:
    All possible ways to reach at index 3 with value 0 are:
    index 5 -> index 4 -> index 1 -> index 3
    index 5 -> index 6 -> index 4 -> index 1 -> index 3
    """
    def canReach(self, arr: List[int], start: int) -> bool:
        def insider(arr, index, seen):
            if index < 0 or index > len(arr) - 1 or index in seen:
                return False
            if arr[index] == 0:
                return True
            seen.add(index)
            return insider(arr, index + arr[index], seen) or insider(arr, index - arr[index], seen)

        return insider(arr, start, set())