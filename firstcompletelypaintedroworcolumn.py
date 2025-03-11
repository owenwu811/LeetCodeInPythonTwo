
#2661
#medium

#You are given a 0-indexed integer array arr, and an m x n integer matrix mat. arr and mat both contain all the integers in the range [1, m * n].

#Go through each index i in arr starting from index 0 and paint the cell in mat containing the integer arr[i].

#Return the smallest index i at which either a row or a column will be completely painted in mat.


#my own solution using python3:

#use a dictionary for rows and columns to track the current row location and current column location, and a final dictionary to track the value to the r, c location 

class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        d = dict()
        rowsd = defaultdict(list)
        colsd = defaultdict(list)
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                d[mat[i][j]] = [i, j]
                rowsd[i].append(mat[i][j])
                colsd[j].append(mat[i][j])
        for i, a in enumerate(arr):
            print(d[a])
            row = d[a][0]
            col = d[a][1]
            if a in rowsd[row]:
                rowsd[row].remove(a)
            if a in colsd[col]:
                colsd[col].remove(a)
            if not rowsd[row] or not colsd[col]:
                return i 
