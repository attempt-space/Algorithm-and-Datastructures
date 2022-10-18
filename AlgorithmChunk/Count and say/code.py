# The count-and-say sequence is a sequence of digit strings defined by the recursive formula:

# countAndSay(1) = "1"
# countAndSay(n) is the way you would "say" the digit string from countAndSay(n-1), which is then converted into a different digit string.
# To determine how you "say" a digit string, split it into the minimal number of substrings such that each substring contains exactly one unique digit. Then for each substring, say the number of digits, then say the digit. Finally, concatenate every said digit.

# For example, the saying and conversion for digit string "3322251":

class Solution:
    def countAndSay(self, n: int) -> str:
        if n==1:
            return "1"
        def helper(integer):
            templist= []
            temp=""
            cnt=1
            for i in range(len(integer)):
                if integer[i] not in templist:
                    templist.append(integer[i])
                if i < len(integer)-1 and integer[i]== integer[i+1]:
                    cnt+=1
                else:
                    prevcount=cnt
                    templist.append(prevcount)
                    temp+= str(templist[1])+str(templist[0])
                    templist= []
                    cnt=1
            return temp
        
        val = 1
        for each in range(1,n):
            val = helper(str(val))
        return val

        