


#1554
#medium

#correct solution after adding hash to get over mle (pretty stupid):

#Given a list of strings dict where all the strings are of the same length.

#Return true if there are 2 strings that only differ by 1 character in the same index, otherwise return false.

 

#Example 1:

#Input: dict = ["abcd","acbd", "aacd"]
#Output: true
#Explanation: Strings "abcd" and "aacd" differ only by one character in the index 1.


class Solution:
    def differByOne(self, dict: List[str]) -> bool:
        seen = set()
        for d in dict:
            for i in range(len(d)):
                cur = d[:i] + "*" + d[i + 1:]
                h = hash(cur)
                if h in seen:
                    return True
                seen.add(h)
        return False
