"""
Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.

The order of output does not matter.

Example 1:

Input:
s: "cbaebabacd" p: "abc"

Output:
[0, 6]

Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
"""
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        from collections import Counter
        if p is None:
            return []
        slength = len(s)
        plength = len(p)
        if slength < plength:
            return []
        sdict = Counter()
        pdict = Counter(p)
        result = []
        for i in range(slength):
            #print(s[i])
            sdict[s[i]] += 1
            #print(sdict)
            if i >= plength:
                if sdict[s[i - plength]] == 1 :
                    del sdict[s[i-plength]]
                else:
                    sdict[s[i - plength]] -=1
            #print(sdict,pdict,i)
            if sdict == pdict:
                result.append(i - plength+1) 
        return result
    
