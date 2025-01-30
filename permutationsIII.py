
#3437
#medium

#Given an integer n, an alternating permutation is a permutation of the first n positive integers such that no two adjacent elements are both odd or both even.

#Return all such alternating permutations sorted in lexicographical order.

 

#Example 1:

#Input: n = 4

#Output: [[1,2,3,4],[1,4,3,2],[2,1,4,3],[2,3,4,1],[3,2,1,4],[3,4,1,2],[4,1,2,3],[4,3,2,1]]

#my own solution using python3:

#generate all permutations according to the parity

class Solution:
    def permute(self, n: int) -> List[List[int]]:
        res = []
        options = list(range(1, n + 1))
        for a in permutations(options):
            #print(a)
            flag = True
            for i in range(1, len(a) - 1):
                if a[i] % 2 == 0 and a[i - 1] % 2 == 0:
                    flag = False
                    break
                if a[i] % 2 != 0 and a[i - 1] % 2 != 0:
                    flag = False
                    break
                if a[i] % 2 == 0 and a[i + 1] % 2 == 0:
                    flag = False
                    break
                if a[i] % 2 != 0 and a[i + 1] % 2 != 0:
                    flag = False
                    break
            if flag:
                print(a)
                res.append(list(a))
        return res
            
