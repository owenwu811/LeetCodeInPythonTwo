
#2672
#medium

#You are given an integer n representing an array colors of length n where all elements are set to 0's meaning uncolored. You are also given a 2D integer array queries where queries[i] = [indexi, colori]. For the ith query:

#Set colors[indexi] to colori.
#Count adjacent pairs in colors set to the same color (regardless of colori).
#Return an array answer of the same length as queries where answer[i] is the answer to the ith query.

 

#Example 1:

#Input: n = 4, queries = [[0,2],[1,2],[3,1],[1,1],[2,1]]

#Output: [0,1,1,0,2]

#Explanation:

#Initially array colors = [0,0,0,0], where 0 denotes uncolored elements of the array.
#After the 1st query colors = [2,0,0,0]. The count of adjacent pairs with the same color is 0.
#After the 2nd query colors = [2,2,0,0]. The count of adjacent pairs with the same color is 1.
#After the 3rd query colors = [2,2,0,1]. The count of adjacent pairs with the same color is 1.
#After the 4th query colors = [2,1,0,1]. The count of adjacent pairs with the same color is 0.
#After the 5th query colors = [2,1,1,1]. The count of adjacent pairs with the same color is 2.


#my own solution using python3:

#keep track of the adjacent pairs and the global maximum

class Solution:
    def colorTheArray(self, n: int, queries: List[List[int]]) -> List[int]: 
        beg = [0] * n
        if len(beg) < 2:
            return [0] * len(queries)
        tot = 0
        res = []
        for q in queries:
            idx = q[0]
            val = q[1]
            beforecnt = 0
            if idx == 0:
                cur, right = beg[idx], beg[idx + 1]
                if cur == right and cur != 0:
                    beforecnt = 1
                else:
                    beforecnt = 0
            elif 1 <= idx <= len(beg) - 2:
                left, cur, right = beg[idx - 1], beg[idx], beg[idx + 1]
                if left == cur == right and cur != 0:
                    beforecnt = 2
                elif left == cur and cur != right and left != 0:
                    beforecnt = 1
                elif left != cur and cur == right and right != 0:
                    beforecnt = 1
                else:
                    beforecnt = 0
            elif idx == len(beg) - 1:
                left, cur = beg[idx - 1], beg[idx]
                if cur == left and cur != 0:
                    beforecnt = 1
                else:
                    beforecnt = 0
            #print(beforecnt)
            beg[idx] = val #change
            aftercnt = 0
            if idx == 0:
                cur, right = beg[idx], beg[idx + 1]
                if cur == right and cur != 0:
                    aftercnt = 1
                else:
                    aftercnt = 0
            elif 1 <= idx <= len(beg) - 2:
                left, cur, right = beg[idx - 1], beg[idx], beg[idx + 1]
                if left == cur == right and cur != 0:
                    aftercnt = 2
                elif left == cur and cur != right and left != 0:
                    aftercnt = 1
                elif left != cur and cur == right and right != 0:
                    aftercnt = 1
                else:
                    aftercnt = 0
            elif idx == len(beg) - 1:
                left, cur = beg[idx - 1], beg[idx]
                if cur == left and cur != 0:
                    aftercnt = 1
                else:
                    aftercnt = 0
            #print(beforecnt, aftercnt)
            diff = aftercnt - beforecnt
            #print(diff)
            tot += diff
            res.append(tot)
        return res
