
#869
#medium

#You are given an integer n. We reorder the digits in any order (including the original order) such that the leading digit is not zero.

#Return true if and only if we can do this so that the resulting number is a power of two.

 

#Example 1:

#Input: n = 1
#Output: true


#correct python3 solution after looking up how to check power of 2:

class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        
        h = str(n)
        for a in permutations(h):
            if a[0] != "0":
                s = ""
                for j in a:
                    s += str(j)
                ints = int(s)
                if math.log2(ints).is_integer() and ints > 0: return True
        return False
