# Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.

# Letters are case sensitive, for example, "Aa" is not considered a palindrome here.

class Solution:
    def longestPalindrome(self, s: str) -> int:
        if len(s) ==1:
            return 1
        stringdict ={}
        for each in s:
            if each not in stringdict:
                stringdict[each] =1
            elif each in stringdict:
                stringdict[each]+=1
        print(stringdict)
        sum = 0
        for key,value in stringdict.items():
            sum += value//2 *2
            if sum %2 ==0 and value %2==1:
                sum+=1
                
        return round(sum)