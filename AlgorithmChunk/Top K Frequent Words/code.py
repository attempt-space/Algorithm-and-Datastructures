# Given an array of strings words and an integer k, return the k most frequent strings.

# Return the answer sorted by the frequency from highest to lowest. Sort the words with the same frequency by their lexicographical order.

# Example 1:

# Input: words = ["i","love","leetcode","i","love","coding"], k = 2
# Output: ["i","love"]
# Explanation: "i" and "love" are the two most frequent words.
# Note that "i" comes before "love" due to a lower alphabetical order.

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
            
        tempdict = OrderedDict()
        for each in words:
            if each not in tempdict:
                tempdict[each] = 1
            else:
                tempdict[each]+=1
        
        tempdict= dict(sorted(tempdict.items(), key=lambda item: (-item[1],item[0])))
        return [key for key, _ in tempdict.items()][:k]
        