#The power of the string is the maximum length of a non-empty substring that contains only one unique character.

#Given a string s, return the power of s.

 

#Example 1:

#Input: s = "leetcode"
#Output: 2
#Explanation: The substring "ee" is of length 2 with the character 'e' only.

class Solution:
    def maxPower(self, s: str) -> int:
        length = len(s)
        maxi = 1
        currentmax = 1
        for i in range(1,length):
        
            if s[i] == s[i-1]:
                currentmax +=1
            else:
                maxi = max(currentmax,maxi)
                currentmax=1
                
                
        return max(currentmax,maxi)
                