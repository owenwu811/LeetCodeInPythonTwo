
#1300
#medium

#Given an integer array arr and a target value target, return the integer value such that when we change all the integers larger than value in the given array to be equal to value, the sum of the array gets as close as possible (in absolute difference) to target.

#In case of a tie, return the minimum such integer.

#Notice that the answer is not neccesarilly a number from arr.

 

#Example 1:

#Input: arr = [4,9,3], target = 10
#Output: 3
#Explanation: When using 3 arr converts to [3, 3, 3] which sums 9 and that's the optimal answer.



#my own solution using python3:

#use the difference and the current array sum being smaller or bigger than the target to make the appropriate decision as to which half to throw away

class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        d = defaultdict(list)
        historical = float('inf')
        l, r = 0, max(arr)
        minkey = float('inf')
        while l <= r:
            new = []
            mid = (l + r) // 2
            for a in arr:
                if a >= mid:
                    new.append(mid)
                else:
                    new.append(a)
            cur = sum(new)
            diff = abs(cur - target)
            d[diff].append(mid)
            minkey = min(minkey, diff)
            if diff >= historical:
                if cursum < target:
                    l = mid + 1
                else:
                    r = mid - 1
            else:
                if cur > target:

                    r = mid - 1
                else:
                    l = mid + 1
        print(d)
        ans = min(d[minkey])
        return ans
        
