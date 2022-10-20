# Example 1:

# Input: num = 3
# Output: "III"
# Explanation: 3 is represented as 3 ones.
# Example 2:

# Input: num = 58
# Output: "LVIII"
# Explanation: L = 50, V = 5, III = 3.

class Solution:
    def intToRoman(self, num: int) -> str:
        
        romandict = OrderedDict()
        romandict = {1000:"M", 900:"CM", 500:"D", 400:"CD", 100:"C", 90:"XC", 50:"L", 40:"XL", 10:"X", 9:"IX", 5:"V", 4:"IV", 1:"I"}
        answerlist= ""
        
        for key,value in romandict.items():
            multiple = num // key
            if multiple:    
                answerlist += value * multiple
                num = num - (multiple * key)
        return answerlist