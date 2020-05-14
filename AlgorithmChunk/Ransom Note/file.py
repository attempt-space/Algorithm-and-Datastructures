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
        
        
        
        
        
