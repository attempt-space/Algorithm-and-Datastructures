"""
Given an arbitrary ransom note string and another string containing letters from all the magazines, write a function that will return true if the ransom note can be constructed from the magazines ; otherwise, it will return false.

Each letter in the magazine string can only be used once in your ransom note.

Input: ransomNote = "aa", magazine = "aab"
Output: true
"""
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        """
        count = 0
        newlist = {}
        
        #Removing Duplicates
        for each in magazine:
            if each in newlist:
                newlist[each] +=1                
            else:
                newlist[each] = 1
        print(newlist)
        for letter in ransomNote:
            if newlist.get(letter) is None or newlist[letter] == 0:
                return False
            else:
                newlist[letter] -=1
        
        return True
        """
        for i in ransomNote:
            if i in magazine:
                magazine = magazine.replace(i,'',1)
            else:
                return False
        return True
        
        
        
        
        
