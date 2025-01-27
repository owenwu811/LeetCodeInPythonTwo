#1267 
#medium

#You are given a map of a server center, represented as a m * n integer matrix grid, where 1 means that on that cell there is a server and 0 means that it is no server. Two servers are said to communicate if they are on the same row or on the same column.

#Return the number of servers that communicate with any other server.

#Input: grid = [[1,0],[0,1]]
#Output: 0
#Explanation: No servers can communicate with others.

#my own solution using python3:

#just keep track of which coordinates have been visited and if it touches x or y from any non equal one

class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        #[[1,0],
        #[0,1]]
        res = 0
        x, y = [], []
        used = []
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    used.append([i, j])
        print(x)
        print(y)
        #[0, 1]
        #[0, 1]
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                flag = False
                if grid[i][j] == 1:
                    for u in used:
                        if i == u[0] and u != [i, j] or j == u[1] and u != [i, j]:
                            print(i, j)
                            flag = True
                            break
                if flag:
                    res += 1


        return res
