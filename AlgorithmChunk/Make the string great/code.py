# Input: s = "leEeetcode"
# Output: "leetcode"
# Explanation: In the first step, either you choose i = 1 or i = 2, both will result "leEeetcode" to be reduced to "leetcode".

class Solution:
    def makeGood(self, s: str) -> str:
        length = len(s)
        liststring = list(s)
        empty = []

        for eachchar in list(s):
            if empty  and (abs(ord(eachchar) - ord(empty[-1])) ==32):
                empty.pop(-1)
            else:
                empty.append(eachchar)
        return ''.join(empty)