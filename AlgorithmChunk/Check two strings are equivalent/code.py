# Input: word1 = ["ab", "c"], word2 = ["a", "bc"]
# Output: true
# Explanation:
# word1 represents string "ab" + "c" -> "abc"
# word2 represents string "a" + "bc" -> "abc"
# The strings are the same, so return true.

class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        firstword = ""
        secondword = ""
        # for each in word1:
        #     firstword+=each
        # for each in word2:
        #     secondword+=each
        firstword="".join(word1)
        secondword="".join(word2)
        return (firstword==secondword)
            