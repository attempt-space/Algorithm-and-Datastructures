"""
Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
"""


class Solution:
    def firstUniqChar(self, s: str) -> int:
        """
        index = 0
        if s is "":
            return -1
        od = OrderedDict() 
        for each in s:
            if each in od:
                od[each] +=1                
            else:
                od[each] = 1   
        for key,value in od.items():
            if value == 1:
                return s.index(key)
        return -1
        """
        letters = "abcdefghijklmnopqrstuvwxyz"
        index=[s.index(l) for l in letters if s.count(l) == 1]
        return min(index) if len(index) > 0 else -1
    
