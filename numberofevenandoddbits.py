#2595
#easy


#You are given a positive integer n.

#Let even denote the number of even indices in the binary representation of n with value 1.

#Let odd denote the number of odd indices in the binary representation of n with value 1.

#Note that bits are indexed from right to left in the binary representation of a number.

#Return the array [even, odd].

 

#Example 1:

#Input: n = 50

#Output: [1,2]

#Explanation:

#The binary representation of 50 is 110010.

#It contains 1 on indices 1, 4, and 5.



#my own solution using python3:

#go from right to left instead of left to right

class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        key = bin(int(n))[2:]
        print(str(key))
        e, o = 0, 0
        for i, a in enumerate(str(key)[::-1]):
            print(a)
            if a == "1":
                if i % 2 == 0:
                    o += 1
                else:
                    e += 1
        return [o, e]
