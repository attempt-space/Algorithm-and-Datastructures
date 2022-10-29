# Given an array of strings strs, group the anagrams together. You can return the answer in any order.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

# Example 1:

# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        localsum = 0
        dict_= {}
        
        for each in strs:
            sortedele = str(sorted(each))
            # print(sortedele)
            if sortedele not in dict_:
                dict_[sortedele] = []
                dict_[sortedele].append(each)
            else:
                dict_[sortedele].append(each)
        returnlist = []
        for key,value in dict_.items():
            returnlist.append(value)
        return returnlist
                