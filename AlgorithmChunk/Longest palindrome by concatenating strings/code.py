# You are given an array of strings words. Each element of words consists of two lowercase English letters.

# Create the longest possible palindrome by selecting some elements from words and concatenating them in any order. Each element can be selected at most once.

# Return the length of the longest palindrome that you can create. If it is impossible to create any palindrome, return 0.

# A palindrome is a string that reads the same forward and backward.

 

# Example 1:

# Input: words = ["lc","cl","gg"]
# Output: 6
# Explanation: One longest palindrome is "lc" + "gg" + "cl" = "lcggcl", of length 6.
# Note that "clgglc" is another longest palindrome that can be created.


class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        dictcount = Counter(words)
        returnval = 0
        center = False
        for key,value in dictcount.items():
            if key[0]  == key[1]:
                if value %2 ==0:
                    returnval += value
                else:
                    returnval +=value -1
                    center = True
            elif  key[0] < key[1]:
                returnval += 2* min(value,dictcount[key[1]+key[0]])
        if center:
            returnval+=1
        return 2* returnval
            