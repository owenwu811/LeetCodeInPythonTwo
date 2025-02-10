#1442
#medium

#Given an array of integers arr.

#We want to select three indices i, j and k where (0 <= i < j <= k < arr.length).

#Let's define a and b as follows:

#a = arr[i] ^ arr[i + 1] ^ ... ^ arr[j - 1]
#b = arr[j] ^ arr[j + 1] ^ ... ^ arr[k]
#Note that ^ denotes the bitwise-xor operation.

#Return the number of triplets (i, j and k) Where a == b.


#my own TLE solution (40 / 47):

class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        res = 0
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                for k in range(j, len(arr)):
                    if i < j <= k:
                        first = arr[i]
                        for a in range(i + 1, j):
                            first = first ^ arr[a]
                        second = arr[j]
                        for b in range(j + 1, k + 1):
                            second = second ^ arr[b]
                        if first == second:
                            res += 1
        return res

#correct python3 solution (could not solve):

class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        n = len(arr)
        prefixXor = [0] * (n + 1)
        
        # Precompute prefix XOR array
        for i in range(n):
            prefixXor[i + 1] = prefixXor[i] ^ arr[i]

        res = 0
        
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                first = prefixXor[j] ^ prefixXor[i]  # XOR of subarray [i:j]
                
                for k in range(j, len(arr)):
                    second = prefixXor[k + 1] ^ prefixXor[j]  # XOR of subarray [j:k+1]
                    if first == second:
                        res += 1
        
        return res
