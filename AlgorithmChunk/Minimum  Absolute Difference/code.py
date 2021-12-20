class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        length = len(arr)
        dict_ = {}
        arr.sort()
        
        returnlist = [[arr[0],arr[1]]]
        min = arr[1]-arr[0]
        
        for i in range(2,length):        
            if abs(arr[i]-arr[i-1]) <= min:
                if (abs(arr[i]-arr[i-1]) == min) and abs(arr[i]-arr[i-1] != 0):
                    tempdict = [arr[i-1],arr[i]]
                    returnlist.append(tempdict) 
                    min = abs(arr[i-1] - arr[i])
                elif abs(arr[i-1]-arr[i] != 0):
                    returnlist = []
                    tempdict = [arr[i-1],arr[i]]
                    returnlist.append(tempdict)
                    min = abs(arr[i-1] - arr[i])
        return returnlist
                    
        
        