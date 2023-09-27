# Given an array of strings strs, group the anagrams together. You can return the answer in any order.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

# Example 1:

# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict_= {}
        
        for each in strs:
            sortedele = "".join(sorted(each))
            if sortedele in dict_:
                dict_[sortedele].append(each)
            else:
                dict_[sortedele]= [each]
        return list(dict_.values())
                