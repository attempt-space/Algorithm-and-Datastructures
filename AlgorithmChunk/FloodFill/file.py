"""
image = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1, sc = 1, newColor = 2
Output: [[2,2,2],[2,2,0],[2,0,1]]
Explanation: 
From the center of the image (with position (sr, sc) = (1, 1)), all pixels connected 
by a path of the same color as the starting pixel are colored with the new color.
Note the bottom corner is not colored 2, because it is not 4-directionally connected
to the starting pixel.
"""
class Solution:
    """
    def recursive(self, image: List[List[int]], sr: int, sc: int,oldColor, newColor: int,rl,cl):
           
        
        if (sr < 0 or sr >= rl or sc < 0 or sc >= cl or image[sr][sc] != oldColor or image[sr][sc] == newColor): 
            return 
  
        image[sr][sc] = newColor
          
        self.recursive(image, sr,sc-1,oldColor,newColor,rl,cl)
        self.recursive(image, sr,sc+1,oldColor,newColor,rl,cl)
        self.recursive(image, sr-1,sc,oldColor,newColor,rl,cl)
        self.recursive(image, sr+1,sc,oldColor,newColor,rl,cl)
        return image
        
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        
        oldColor = image[sr][sc]
        rl = len(image)
        cl = len(image[sr])
        if image[sr][sc] == newColor:
            return image
        return self.recursive(image,sr,sc,oldColor,newColor,rl,cl)
    """
    initialColor, rows, cols = image[sr][sc], len(image), len(image[0])
    def spread(row, col):
        if 0 > row or row >= rows or 0 > col or col >= cols:
            return
        if image[row][col] == newColor or image[row][col] != initialColor:
            return
        image[row][col] = newColor
        spread(row+1, col)
        spread(row-1, col)
        spread(row, col+1)
        spread(row, col-1)
    spread(sr, sc)
    return image

        
