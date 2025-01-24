"""
Input: graph = [[1,2],[2,3],[5],[0],[5],[],[]]
Output: [2,4,5,6]
"""

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        visited = [0]*len(graph)
        def has_cycle(node):
            if visited[node] == 1:
                return True
            if visited[node] == 2:
                return False
            visited[node] = 1
            for neigh in graph[node]:
                if has_cycle(neigh):
                    return True

            visited[node] =2
            return False
        
        return [node for node in range(len(graph)) if not has_cycle(node)]  
