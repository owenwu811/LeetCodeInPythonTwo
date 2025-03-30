#3199
#easy

#Given three integer arrays a, b, and c, return the number of triplets (a[i], b[j], c[k]), such that the bitwise XOR of the elements of each triplet has an even number of set bits.
 

#Example 1:

#Input: a = [1], b = [2], c = [3]

#Output: 1

#Explanation:

#The only triplet is (a[0], b[0], c[0]) and their XOR is: 1 XOR 2 XOR 3 = 002.



#my own solution using python3:

#just triple loop it and follow the instructions

class Solution:
    def tripletCount(self, a: List[int], b: List[int], c: List[int]) -> int:
        res = 0
        for i in range(len(a)):
            for j in range(len(b)):
                for k in range(len(c)):
                    first = bin(a[i])[2:]
                    second = bin(b[j])[2:]
                    third = bin(c[k])[2:]
                    if (first.count("1") + second.count("1") + third.count("1")) % 2 == 0:
                        res += 1
        return res
