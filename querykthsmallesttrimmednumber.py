

#2343
#medium
#You are given a 0-indexed array of strings nums, where each string is of equal length and consists of only digits.

#You are also given a 0-indexed 2D integer array queries where queries[i] = [ki, trimi]. For each queries[i], you need to:

#Trim each number in nums to its rightmost trimi digits.
#Determine the index of the kith smallest trimmed number in nums. If two trimmed numbers are equal, the number with the lower index is considered to be smaller.
#Reset each number in nums to its original length.
#Return an array answer of the same length as queries, where answer[i] is the answer to the ith query.

#Note:

#To trim to the rightmost x digits means to keep removing the leftmost digit, until only x digits remain.
#Strings in nums may contain leading zeros.

#correct python3 solution (could not solve) - question lacks enough informatino to solve:


class Solution:
    def smallestTrimmedNumbers(self, nums: List[str], queries: List[List[int]]) -> List[int]:
        ans = []
        for q in queries:
            k, trim = q[0], q[1] 
            l1 = [(num[-trim:], i) for i, num in enumerate(nums)]
            l1.sort()
            ans.append(l1[k - 1][1])
            #l1 = [(num[-trim:], i) for i, num in enumerate(nums)]
            #l1.sort()
            #l.append(l1[k - 1][1])
        return ans
