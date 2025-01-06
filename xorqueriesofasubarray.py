
#1310
#medium

#You are given an array arr of positive integers. You are also given the array queries where queries[i] = [lefti, righti].

#For each query i compute the XOR of elements from lefti to righti (that is, arr[lefti] XOR arr[lefti + 1] XOR ... XOR arr[righti] ).

#Return an array answer where answer[i] is the answer to the ith query.

 

#Example 1:

#Input: arr = [1,3,4,8], queries = [[0,1],[1,2],[0,3],[3,3]]
#Output: [2,7,14,8] 
#Explanation: 
#The binary representation of the elements in the array are:
#1 = 0001 
#3 = 0011 
#4 = 0100 
#8 = 1000 
#The XOR values for queries are:
#[0,1] = 1 xor 3 = 2 
#[1,2] = 3 xor 4 = 7 
#[0,3] = 1 xor 3 xor 4 xor 8 = 14 
#[3,3] = 8


#my solution that got TLE 41/46:

class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        ans = []
        for q in queries:
            tmp = []
            for i in range(q[0], q[1] + 1):
                tmp.append(arr[i])
            starting = tmp[0]
            for i in range(1, len(tmp)):
                starting = starting ^ tmp[i]
            ans.append(starting)
        return ans


#correct python3 solution (could not solve):

class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        prefixarr = [arr[0]]
        for i in range(1, len(arr)):
            arr[i] = arr[i - 1] ^ arr[i]
            prefixarr.append(arr[i])
        res = []
        for q in queries:
            if q[0] == 0: #everything from the beginning
                res.append(prefixarr[q[1]])
            else:
                res.append(prefixarr[q[1]] ^ prefixarr[q[0] - 1])
        return res
