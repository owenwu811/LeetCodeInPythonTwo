
#432
#Hard

#Design a data structure to store the strings' count with the ability to return the strings with minimum and maximum counts.

#Implement the AllOne class:

#AllOne() Initializes the object of the data structure.
#inc(String key) Increments the count of the string key by 1. If key does not exist in the data structure, insert it with count 1.
#dec(String key) Decrements the count of the string key by 1. If the count of key is 0 after the decrement, remove it from the data structure. It is guaranteed that key exists in the data structure before the decrement.
#getMaxKey() Returns one of the keys with the maximal count. If no element exists, return an empty string "".
#getMinKey() Returns one of the keys with the minimum count. If no element exists, return an empty string "".
#Note that each function must run in O(1) average time complexity.

#my own solution using python3:

#just do exactly as asked

class AllOne:

    def __init__(self):
        self.d = defaultdict(int)
        
    def inc(self, key: str) -> None:
        self.d[key] += 1
        

    def dec(self, key: str) -> None: 
        self.d[key] -= 1
        if self.d[key] == 0:
            del self.d[key]
        

    def getMaxKey(self) -> str:
        if self.d:
            biggest = max(self.d.values())
            for k in self.d:
                if self.d[k] == biggest:
                    return k
        return ""
    def getMinKey(self) -> str:
        if self.d:
            smallest = min(self.d.values())
            for k in self.d:
                if self.d[k] == smallest:
                    return k
        return ""
            


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()
