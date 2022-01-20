# You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

# Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule.

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        length = len(flowerbed)
        count = 0
        for each in range(length):
            if flowerbed[each] == 0:
                prev= 0 if (each ==0 or flowerbed[each-1] ==0) else 1
                next= 0 if (each == length-1 or flowerbed[each+1] ==0) else 1
                print(prev,next)
                if (prev ==0 and next ==0):
                    flowerbed[each]=1
                    count+=1
            if count >=n:
                return True
            
        return count>=n