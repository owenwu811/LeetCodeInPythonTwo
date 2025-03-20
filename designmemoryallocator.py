#2502
#medium

#You are given an integer n representing the size of a 0-indexed memory array. All memory units are initially free.

#You have a memory allocator with the following functionalities:

#Allocate a block of size consecutive free memory units and assign it the id mID.
#Free all memory units with the given id mID.
#Note that:

#Multiple blocks can be allocated to the same mID.
#You should free all the memory units with mID, even if they were allocated in different blocks.
#Implement the Allocator class:

#Allocator(int n) Initializes an Allocator object with a memory array of size n.
#int allocate(int size, int mID) Find the leftmost block of size consecutive free memory units and allocate it with the id mID. Return the block's first index. If such a block does not exist, return -1.
#int freeMemory(int mID) Free all memory units with the id mID. Return the number of memory units you have freed.


#my own solution using python3:

#use prefix sums to get the sum of a subarray 

class Allocator:

    def __init__(self, n: int):
        self.cur = [-1] * n
        self.curlen = n

    def allocate(self, size: int, mID: int) -> int:
        now = []
        b = list(itertools.accumulate(self.cur))
        #print(self.cur, b)
        if min(self.cur) == -1:
            a = self.cur.index(-1)
            for i in range(a, self.curlen - size + 1):
                if self.cur[i] == -1:
                    if i + size <= self.curlen:
                        if i <= 0:
                            u = b[i + size - 1]
                        else:
                            u = b[i + size - 1] - b[i - 1]
                        if u == -1 * size:
                            self.cur[i: i + size] = [mID] * size
                            now.append(i)
                            #print(self.cur)
                            if now:
                                return now[0]
                            else:
                                return 0
                            
                    else:
                        return -1
        return -1
        
    def freeMemory(self, mID: int) -> int:
        res = 0
        for i in range(len(self.cur)):
            if self.cur[i] == mID:
                self.cur[i] = -1
                res += 1
        return res

# Your Allocator object will be instantiated and called as such:
# obj = Allocator(n)
# param_1 = obj.allocate(size,mID)
# param_2 = obj.freeMemory(mID)
