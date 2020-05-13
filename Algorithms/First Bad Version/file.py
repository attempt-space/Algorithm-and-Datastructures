#Given n = 5, and version = 4 is the first bad version.

#call isBadVersion(3) -> false
#call isBadVersion(5) -> true
#call isBadVersion(4) -> true

#Then 4 is the first bad version. 



# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<2:
            return n
        left = 1
        right = n
        while left <= right: 
            mid = (left+right)//2;
            if (isBadVersion(mid)) and not isBadVersion(mid-1):
                return mid
            elif isBadVersion(mid-1):
                right = mid - 1;
            else:
                left = mid + 1;
                    
