#1664
#medium

#You are given an integer array nums. You can choose exactly one index (0-indexed) and remove the element. Notice that the index of the elements may change after the removal.

#For example, if nums = [6,1,7,4,1]:

#Choosing to remove index 1 results in nums = [6,7,4,1].
#Choosing to remove index 2 results in nums = [6,1,4,1].
#Choosing to remove index 4 results in nums = [6,1,7,4].
#An array is fair if the sum of the odd-indexed values equals the sum of the even-indexed values.

#Return the number of indices that you could choose such that after the removal, nums is fair.

 

#Example 1:

#Input: nums = [2,1,6,4]
#Output: 1
#Explanation:
#Remove index 0: [1,6,4] -> Even sum: 1 + 4 = 5. Odd sum: 6. Not fair.
#Remove index 1: [2,6,4] -> Even sum: 2 + 4 = 6. Odd sum: 6. Fair.
#Remove index 2: [2,1,4] -> Even sum: 2 + 4 = 6. Odd sum: 1. Not fair.
#Remove index 3: [2,1,6] -> Even sum: 2 + 6 = 8. Odd sum: 1. Not fair.
#There is 1 index that you can remove to make nums fair.


#my own solution using python3:

#think before is normal after is flipped in terms of even vs. odd

class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        d = defaultdict(list)
        res = 0
        esize, osize = 0, 0
        aftereven, afterodd = 0, 0
        for i, val in enumerate(nums):
            if i % 2 == 0:
                d["e"].append(i)
                esize += 1
            else:
                d["o"].append(i)
                osize += 1
        orig = nums.copy()
        el = []
        for a in d["e"]:
            el.append(orig[a])
        ol = []
        for a in d["o"]:
            ol.append(orig[a])
        ep = list(itertools.accumulate(el))
        op = list(itertools.accumulate(ol))
        beforeeven, beforeodd = 0, 0
        for i in range(len(nums)):
            if i % 2 == 0:
                afterodd -= nums[i]
            elif i % 2 != 0:
                aftereven -= nums[i]
            if i >= 1:
                if i % 2 == 0:
                    beforeodd += nums[i - 1]
                else:
                    beforeeven += nums[i - 1]
            val = nums[i]
            nums.pop(i)
            beven = bisect_right(d["e"], i)
            bodd = bisect_right(d["o"], i)
            e, o = 0, 0
            if el:
                if beven <= 0:
                    o = ep[-1]
                else:
                    o = ep[-1] - ep[beven - 1]
            if ol:
                if bodd <= 0:
                    e = op[-1]
                else:
                    e = op[-1] - op[bodd - 1]
                    #o = sum(el[beven:])
                    #e = sum(ol[bodd:])
            if beforeeven + e == beforeodd + o:
                res += 1
            nums.insert(i, val)
        return res
