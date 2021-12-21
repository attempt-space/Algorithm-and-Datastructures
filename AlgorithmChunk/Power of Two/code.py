class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
#         for each in range(31):
#             if ((2 ** each) == n) and (2** each) <= n:
#                 return True
            
#             elif (2** each) >n:
#                 return False        
        
        return n and not (n & n - 1)