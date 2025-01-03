
#119
#easy

#Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.

#In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

#Input: rowIndex = 3
#Output: [1,3,3,1]

#my own solution using python3:

#make observations that the current is the sum of the previous minus one plus the previous

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res = []
        for i in range(1, rowIndex + 2):
            res.append([1] * i)
        print(res)
        for i in range(2, len(res)):
            print(res[i])
            for j in range(1, len(res[i]) - 1):
                print(j)
                res[i][j] = res[i - 1][j - 1] + res[i - 1][j]
        print(res)
        return res[rowIndex]
