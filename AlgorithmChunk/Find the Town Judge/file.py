"""
In a town, there are N people labelled from 1 to N.  There is a rumor that one of these people is secretly the town judge.

If the town judge exists, then:

The town judge trusts nobody.
Everybody (except for the town judge) trusts the town judge.
There is exactly one person that satisfies properties 1 and 2.
You are given trust, an array of pairs trust[i] = [a, b] representing that the person labelled a trusts the person labelled b.

If the town judge exists and can be identified, return the label of the town judge.  Otherwise, return -1.
Example 3:

Input: N = 3, trust = [[1,3],[2,3],[3,1]]
Output: -1
Example 4:

Input: N = 3, trust = [[1,2],[2,3]]
Output: -1
Example 5:

Input: N = 4, trust = [[1,3],[1,4],[2,3],[2,4],[4,3]]
Output: 3

 """

class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        finaldict = {}
        listofall = []
        if N == 1 and not trust:
            return N
            
        for each in trust:
            [x,y] = each
            listofall.append(x)
            if y in finaldict:
                finaldict[y] += 1
            else:
                finaldict[y] = 1
        for key,value in finaldict.items():
            if value == N-1 and key not in listofall:
                return key
            
        return -1 
            
  
