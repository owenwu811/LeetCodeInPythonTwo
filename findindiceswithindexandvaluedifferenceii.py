#2905
#medium

#You are given a 0-indexed integer array nums having length n, an integer indexDifference, and an integer valueDifference.

#Your task is to find two indices i and j, both in the range [0, n - 1], that satisfy the following conditions:

#abs(i - j) >= indexDifference, and
#abs(nums[i] - nums[j]) >= valueDifference
#Return an integer array answer, where answer = [i, j] if there are two such indices, and answer = [-1, -1] otherwise. If there are multiple choices for the two indices, return any of them.

#Note: i and j may be equal.

 

#Example 1:

#Input: nums = [5,1,4,1], indexDifference = 2, valueDifference = 4
#Output: [0,3]
#Explanation: In this example, i = 0 and j = 3 can be selected.
#abs(0 - 3) >= 2 and abs(nums[0] - nums[3]) >= 4.
#Hence, a valid answer is [0,3].
#[3,0] is also a valid answer.

#my own solution using python3:

#use binary search for the left and right sides

class Solution:
    def findIndices(self, nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:
        
        d = defaultdict(list)
        for i, n in enumerate(nums):
            d[n].append(i)
        lefts = []
        for i in range(indexDifference, len(nums)):
            l = bisect_left(lefts, nums[i - indexDifference])
            lefts.insert(l, nums[i - indexDifference])
            #lefts.add(nums[i - indexDifference])
            bl = bisect_left(lefts, nums[i] - valueDifference) 
            br = bisect_left(lefts, nums[i] + valueDifference)
            if bl < len(lefts):
                if abs(lefts[bl] - nums[i]) >= valueDifference:
                    return [d[lefts[bl]][0], i]
            if bl - 1 >= 0 and bl - 1 < len(lefts):
                if abs(lefts[bl - 1] - nums[i]) >= valueDifference:
                    return [d[lefts[bl - 1]][0], i]
            if br < len(lefts):
                if abs(lefts[br] - nums[i]) >= valueDifference:
                    return [d[lefts[br]][0], i]
        rights = SortedList(nums[indexDifference:])
        for i in range(len(nums) - indexDifference):
            bl = bisect_left(rights, nums[i] - valueDifference)
            br = bisect_left(rights, nums[i] + valueDifference)
            if bl < len(rights):
                if abs(rights[bl] - nums[i]) >= valueDifference:
                    return [d[rights[bl]][0], i]
            if br < len(rights):
                if abs(rights[br] - nums[i]) >= valueDifference:
                    return [d[rights[br]][0], i]
            rights.discard(nums[i + indexDifference - 1])
        return [-1, -1]
