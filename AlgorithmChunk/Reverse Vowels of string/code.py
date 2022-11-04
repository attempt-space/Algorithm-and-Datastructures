# Given a string s, reverse only all the vowels in the string and return it.

# The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

# Example 1:

# Input: s = "hello"
# Output: "holle"

class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = 'aeiouAEIOU'
        left = 0
        right = len(s)-1
        strtolist = list(s)
        while left <right:
            if strtolist[left] in vowels and strtolist[right] in vowels:
                strtolist[left],strtolist[right] = strtolist[right],strtolist[left]
                left +=1
                right -=1
            elif strtolist[left] not in vowels:
                left +=1
            else:
                right-=1
                
        return ''.join(strtolist)
                