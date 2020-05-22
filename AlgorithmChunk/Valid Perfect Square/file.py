"""
Given a positive integer num, write a function which returns True if num is a perfect square else False.

Follow up: Do not use any built-in library function such as sqrt.

Input: num = 16
Output: true

"""
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num == 1:
            return 1
       
        min = 1
        max = num //2 + 1
        
        
        while min <= max :
            median = (min + max)//2
            
            val = median * median
            
            if val == num:
                return True
            elif val > num:
                max = median - 1
            elif val < num:
                min = median + 1

        return False
        
