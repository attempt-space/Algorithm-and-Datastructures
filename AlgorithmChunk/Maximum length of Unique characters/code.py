#  Maximum Length of a Concatenated String with Unique Characters
# You are given an array of strings arr. A string s is formed by the concatenation of a subsequence of arr that has unique characters.

# Return the maximum possible length of s.

# A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.
# Input: arr = ["un","iq","ue"]
# Output: 4
# Explanation: All the valid concatenations are:
# - ""
# - "un"
# - "iq"
# - "ue"
# - "uniq" ("un" + "iq")
# - "ique" ("iq" + "ue")
# Maximum length is 4.

class Solution:
    def maxLength(self, arr: List[str]) -> int:
        sz, combinedWords, maxLength = len(arr), [''], 0
        # Iterate over every string present in arr
        for string in arr:

            for word in combinedWords:
                resultantWord = word + string
                if len(resultantWord) != len(set(resultantWord)):
                    continue
                combinedWords.append(resultantWord)
                maxLength = max(maxLength, len(resultantWord))
        return maxLength