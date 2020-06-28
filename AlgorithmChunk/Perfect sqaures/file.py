"""
Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

Example 1:

Input: n = 12
Output: 3 
Explanation: 12 = 4 + 4 + 4.
Example 2:

Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.

 Lagrange’s four-square theorem
"""
class Solution:
    def numSquares(self, n: int) -> int:
        # Create a dynamic programming table 
        # to store sq and getMinSquares table 
        # for base case entries 
        while n % 4 == 0:
            n /= 4
        if n % 8 == 7:
            return 4
        i = 0
        print(n)
        while i * i < n:		
            
            j = int(sqrt(n - i * i))	
            print(i,j)
            if i * i + j * j == n:
                print(i,j)
                return (i > 0) + (j > 0)
            i += 1
        return 3
