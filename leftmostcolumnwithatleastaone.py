
#1428
#medium

#A row-sorted binary matrix means that all elements are 0 or 1 and each row of the matrix is sorted in non-decreasing order.

#Given a row-sorted binary matrix binaryMatrix, return the index (0-indexed) of the leftmost column with a 1 in it. If such an index does not exist, return -1.

#You can't access the Binary Matrix directly. You may only access the matrix using a BinaryMatrix interface:

#BinaryMatrix.get(row, col) returns the element of the matrix at index (row, col) (0-indexed).
#BinaryMatrix.dimensions() returns the dimensions of the matrix as a list of 2 elements [rows, cols], which means the matrix is rows x cols.
#Submissions making more than 1000 calls to BinaryMatrix.get will be judged Wrong Answer. Also, any solutions that attempt to circumvent the judge will result in disqualification.

#For custom testing purposes, the input will be the entire binary matrix mat. You will not have access to the binary matrix directly.


#my own solution using python3:

# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, row: int, col: int) -> int:
#    def dimensions(self) -> list[]:

#you know that ones are the rightmost alignment of every row, so binary search on each row

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        ans = float('inf')
        x, y = binaryMatrix.dimensions()
        #(0, 0), (0, 1)
        #[[0, 0]]
        #[[1, 1]]

        #ones always are to the right most 
        #[[1,1,1,1,1],
        #[0,0,0,1,1],
        #[0,0,1,1,1],
        #[0,0,0,0,1],
        #[0,0,0,0,0]]

        for i in range(x):
            val = binaryMatrix.get(i, i)
            #print(val)
            l, r = 0, binaryMatrix.dimensions()[0] - 1
            print(l, r)
            while l <= r:
                mid = (l + r) // 2
                cur = binaryMatrix.get(i, mid)
                if cur == 1:
                    ans = min(ans, mid)
                    r = mid - 1
                else:
                    l = mid + 1
            #ans = min(ans, l)
            
            
        if ans == float('inf'): return -1
        return ans
