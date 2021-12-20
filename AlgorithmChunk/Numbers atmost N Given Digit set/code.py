# Given an array of digits which is sorted in non-decreasing order. You can write numbers using each digits[i] as many times as we want. For example, if digits = ['1','3','5'], we may write numbers such as '13', '551', and '1351315'.

# Return the number of positive integers that can be generated that are less than or equal to a given integer n.

 

# Example 1:

# Input: digits = ["1","3","5","7"], n = 100
# Output: 20
# Explanation: 
# The 20 numbers that can be written are:
# 1, 3, 5, 7, 11, 13, 15, 17, 31, 33, 35, 37, 51, 53, 55, 57, 71, 73, 75, 77.

class Solution:
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
        strnum = str(n)
        count = 0
        
        for i in range(1,len(strnum)):
            count = count + (len(digits) ** i)
            print(len(strnum) ** i,"+")
                
        i = 0
        #strnum = 4
        while i < len(strnum):
            j = 0
            print("i",i,digits)
            while (j < len(digits)) and (digits[j] < strnum[i]):
                count += (len(digits) ** (len(strnum)-i-1))
                print(len(digits) ** (len(strnum)-i-1),"+", end =" ")
                j+=1
            if (j == len(digits)) or (digits[j] > strnum[i]):
                return count               
            i+=1
            
        count+=1
        
        return count