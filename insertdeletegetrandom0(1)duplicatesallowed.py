#381
#hard

#RandomizedCollection is a data structure that contains a collection of numbers, possibly duplicates (i.e., a multiset). It should support inserting and removing specific elements and also reporting a random element.

#Implement the RandomizedCollection class:

#RandomizedCollection() Initializes the empty RandomizedCollection object.
#bool insert(int val) Inserts an item val into the multiset, even if the item is already present. Returns true if the item is not present, false otherwise.
#bool remove(int val) Removes an item val from the multiset if present. Returns true if the item is present, false otherwise. Note that if val has multiple occurrences in the multiset, we only remove one of them.
#int getRandom() Returns a random element from the current multiset of elements. The probability of each element being returned is linearly related to the number of the same values the multiset contains.
#You must implement the functions of the class such that each function works on average O(1) time complexity.

#Note: The test cases are generated such that getRandom will only be called if there is at least one item in the RandomizedCollection.


#my own solution using python3:

#just use the built in random.choice module

class RandomizedCollection:

    def __init__(self):
        self.cur = SortedList()
        self.turn = 0
        
    def insert(self, val: int) -> bool:
        if val not in self.cur:
            self.cur.add(val)
            return True  
        self.cur.add(val)
        return False
        

    def remove(self, val: int) -> bool:
        if val in self.cur:
            self.cur.remove(val)
            return True  
        return False
        
    def getRandom(self) -> int:
        return random.choice(self.cur)
        


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
