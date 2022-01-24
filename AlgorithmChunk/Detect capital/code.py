# We define the usage of capitals in a word to be right when one of the following cases holds:

# All letters in this word are capitals, like "USA".
# All letters in this word are not capitals, like "leetcode".
# Only the first letter in this word is capital, like "Google".
# Given a string word, return true if the usage of capitals in it is right.

 

class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        length = len(word)
        count=0
        for i in range(length):
            if (ord(word[i])>=ord("A")) and (ord(word[i])<= ord("Z")):
                count+=1
        print(count) 
        if count ==0 or count == length:
            return True
        if count ==1 and (ord(word[0]) >=ord("A") and ord(word[0])<= ord("Z")):
            return True
        
        return False
        
        