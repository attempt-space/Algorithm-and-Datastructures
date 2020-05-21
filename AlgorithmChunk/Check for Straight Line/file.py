"""
You are given an array coordinates, coordinates[i] = [x, y], where [x, y] represents the coordinate of a point. Check if these points make a straight line in the XY plane.
Input: coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
Output: true
"""
class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        
        length = len(coordinates)
        
        if length ==2:
            return True
        [x0,y0] = coordinates[0]
        [x1,y1] = coordinates[1]
        
        xisconstant = False
        yisconstant = False
        slope = None
        intercept = None
        
        if x0 ==x1:
            xisconstant = True
        elif y0 == y1:
            yisconstant = True
        else:    
            slope = (y1 - y0) / (x1 - x0)
            intercept = y0 - (slope * x0)
            
        for i in range(1,length):
            
            each = coordinates[i] 
            if xisconstant and x0 != each[0] :
                return False
            
            elif yisconstant and y0 != each[1]:
                return False
            
            elif not xisconstant and not yisconstant and  (each[0]* slope + intercept) != each[1]:
                return False
        return True
        
