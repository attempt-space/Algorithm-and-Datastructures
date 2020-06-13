class RandomizedSet:
    """
    this solution has long time but confined to single array
    def __init__(self):
        
        self.arraylist = []
        

    def insert(self, val: int) -> bool:
        if val not in self.arraylist:
            self.arraylist.append(val)
            return True
        else:
            
            return False
        

    def remove(self, val: int) -> bool:
        if val in self.arraylist:
            self.arraylist.remove(val)
            return True
        else:
            return False
        
    def getRandom(self) -> int:
        if len(self.arraylist) == 0:
            return False
        else:
            import random
            return random.choice(self.arraylist)
    Elegant solution     
    """
    import random
    def __init__(self):
        self.index = {}
        self.set = []
        

    def insert(self, val: int) -> bool:
        if val in self.index:
            return False
        self.set.append(val)
        self.index[val] = len(self.set) - 1
        return True
        

    def remove(self, val: int) -> bool:
        print(self.index)
        print(self.set)
        if val not in self.index:
            return False
        i = self.index[val]
        self.set[i] = self.set[-1]
        self.index[self.set[i]] = i
        print(self.set)
        print(self.index)
        del self.set[-1]
        del self.index[val]
        return True
        

    def getRandom(self) -> int:
        return random.choice(self.set)
        



# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
