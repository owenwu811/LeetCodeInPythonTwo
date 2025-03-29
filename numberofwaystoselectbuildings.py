#2222
#medium


#You are given a 0-indexed binary string s which represents the types of buildings along a street where:

#s[i] = '0' denotes that the ith building is an office and
#s[i] = '1' denotes that the ith building is a restaurant.
#As a city official, you would like to select 3 buildings for random inspection. However, to ensure variety, no two consecutive buildings out of the selected buildings can be of the same type.

#For example, given s = "001101", we cannot select the 1st, 3rd, and 5th buildings as that would form "011" which is not allowed due to having two consecutive buildings of the same type.
#Return the number of valid ways to select 3 buildings.

 

#Example 1:

#Input: s = "001101"
#Output: 6



#my own solution using python3:

#left side times right side

class Solution:
    def numberOfWays(self, s: str) -> int:
        res = 0
        left = Counter()
        left[s[0]] += 1
        right = Counter(s[1:])
        for i in range(1, len(s) - 1):
            cur = s[i]
            left[s[i]] += 1
            right[s[i]] -= 1
            if right[s[i]] == 0:
                del right[s[i]]
            if cur == "1":
                res += (left["0"] * right["0"])
            else:
                res += (left["1"] * right["1"])
        return res
