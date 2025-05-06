#3391
#medium

#You are given a n x n x n binary 3D array matrix.

#Implement the Matrix3D class:

#Matrix3D(int n) Initializes the object with the 3D binary array matrix, where all elements are initially set to 0.
#void setCell(int x, int y, int z) Sets the value at matrix[x][y][z] to 1.
#void unsetCell(int x, int y, int z) Sets the value at matrix[x][y][z] to 0.
#int largestMatrix() Returns the index x where matrix[x] contains the most number of 1's. If there are multiple such indices, return the largest x.
 

#Example 1:

#Input:
#["Matrix3D", "setCell", "largestMatrix", "setCell", "largestMatrix", "setCell", "largestMatrix"]
#[[3], [0, 0, 0], [], [1, 1, 2], [], [0, 0, 1], []]

#Output:
#[null, null, 0, null, 1, null, 0]

#my own solution using python3:

#use multiple dictionaries

class Matrix3D:

    def __init__(self, n: int):
        self.d = defaultdict(int)
        self.freq = defaultdict(int)
        self.a = defaultdict(SortedList)
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    self.d[(i, j, k)] = 0
                    self.freq[(i, "z")] += 1
                    self.freq[(i, "o")] = 0
            self.a[i].add(0)

    def setCell(self, x: int, y: int, z: int) -> None:
        before = self.d[(x, y, z)]
        self.d[(x, y, z)] = 1
        if before == 0:
            self.a[x].discard(0)
            self.a[x].add(1)
        self.freq[(x, "o")] += 1
        if self.freq[(x, "z")] > 0:
            self.freq[(x, "z")] -= 1
        
    def unsetCell(self, x: int, y: int, z: int) -> None:
        before = self.d[(x, y, z)]
        self.d[(x, y, z)] = 0
        if before == 1:
            self.a[x].discard(1)
            self.a[x].add(0)
        if self.freq[(x, "o")] > 0:
            self.freq[(x, "o")] -= 1
        self.freq[(x, "z")] += 1
        
    def largestMatrix(self) -> int:
        now = SortedList()
        #print(self.a)
        for k in self.a:
            now.add((self.a[k].count(1), k))
        return now[-1][-1]

# Your Matrix3D object will be instantiated and called as such:
# obj = Matrix3D(n)
# obj.setCell(x,y,z)
# obj.unsetCell(x,y,z)
# param_3 = obj.largestMatrix()
