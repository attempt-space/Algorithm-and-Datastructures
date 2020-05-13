"""

You're given strings J representing the types of stones that are jewels, and S representing the stones you have.  Each character in S is a type of stone you have.  You want to know how many of the stones you have are also jewels.

The letters in J are guaranteed distinct, and all characters in J and S are letters. Letters are case sensitive, so "a" is considered a different type of stone from "A".

Input: J = "aA", S = "aAAbbbb"
Output: 3

"""

class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        """
        count = 0
        newlist = {}
        #Removing Duplicates
        for each in S:
            if each in newlist:
                newlist[each] +=1                
            else:
                newlist[each] = 1
                
        for each in J:
            if each in newlist:
                count = count + newlist[each]
                
        return count
        """
        return sum (s in J for s in S)
