"""
Example 1:

Input: ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
Example 2:

Input: ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]
"""

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        lengthOfString = len(s)

        for i in range(lengthOfString//2):
            s[i],s[lengthOfString-i-1] = s[lengthOfString-i-1],s[i]
