"""
Given a positive integer num, output its complement number. The complement strategy is to flip the bits of its binary representation.

Input: num = 5
Output: 2
Explanation: The binary representation of 5 is 101 (no leading zero bits), and its complement is 010. So you need to output 2.
"""

class Solution:
    def findComplement(self, num: int) -> int:
        """
        count = 0 
        sum = 0
        binary = ""
        while num !=0:
            if num ==1:
                binary = binary + str(0)
                break
            elif num % 2 == 0:
                binary= binary + str(1)
            elif num % 2 == 1:
                binary= binary + str(0)
            num = num//2
        binary = binary[::-1]

        binary = int(binary)
        
        while binary > 0:
            sum = sum + pow(2,count) * (binary % 10)
            binary = binary//10
            count+=1    
        return sum
        """
        temp = num
        bit =1
        while temp!=0:
            num = num^bit
            print(num)
            bit= bit << 1
            temp= temp >>1
        return num
        
