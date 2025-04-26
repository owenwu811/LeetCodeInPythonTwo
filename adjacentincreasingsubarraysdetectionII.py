
#3350
#medium

#Given an array nums of n integers, your task is to find the maximum value of k for which there exist two adjacent subarrays of length k each, such that both subarrays are strictly increasing. Specifically, check if there are two subarrays of length k starting at indices a and b (a < b), where:

#Both subarrays nums[a..a + k - 1] and nums[b..b + k - 1] are strictly increasing.
#The subarrays must be adjacent, meaning b = a + k.
#Return the maximum possible value of k.

#A subarray is a contiguous non-empty sequence of elements within an array.

 

#Example 1:

#Input: nums = [2,5,7,8,9,2,3,4,3,1]

#Output: 3

#Explanation:

#The subarray starting at index 2 is [7, 8, 9], which is strictly increasing.
#The subarray starting at index 5 is [2, 3, 4], which is also strictly increasing.
#These two subarrays are adjacent, and 3 is the maximum possible value of k for which two such adjacent strictly increasing subarrays exist.

#my own solution using python3:

#use binary search to find the best size

class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        l, r = 1, len(nums) // 2 
        pref = []
        for i in range(len(nums) - 1):
            if nums[i] >= nums[i + 1]:
                pref.append("b")
            else:
                pref.append("g")
        pref.append("g")
        n = len(nums)
        ans = 0
        while l <= r:
            mid = (l + r) // 2
            size = mid
            d = defaultdict(int)
            c = Counter(pref[:size - 1])
            dd = deque(nums[:size])
            #a = SortedSet()
            for i in range(n - size + 1):
                if mid == 1:
                    flag = True
                elif not c["b"]:
                    flag = True
                else:
                    flag = False
                if flag:
                    d[i] = "a"
                c[pref[i]] -= 1
                dd.popleft()
                if c[pref[i]] <= 0:
                    del c[pref[i]]
                c[pref[i + size - 1]] += 1
                dd.append(nums[i + size - 1])

            ff = False
            a = SortedSet(d.keys())
            for val in a:
                if val + size in d:
                    ff = True
                    break
                if val + size > a[-1]:
                    ff = False
                    break
            if ff:
                ans = max(ans, mid)
                l = mid + 1
            else:
                r = mid - 1
        return ans
